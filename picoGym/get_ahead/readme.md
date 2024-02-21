# GET aHEAD

## Description
```
Find the flag being held on this server to get ahead of the competition http://mercury.picoctf.net:28916/
```

## Writeup

We should start off by taking a look at website. <br/>
```html
<!doctype html>
<html>
<head>
    <title>Blue</title>
    <link rel="stylesheet" type="text/css" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
	<style>body {background-color: blue;}</style>
</head>
	<body>
		<div class="container">
			<div class="row">
				<div class="col-md-6">
					<div class="panel panel-primary" style="margin-top:50px">
						<div class="panel-heading">
							<h3 class="panel-title" style="color:red">Red</h3>
						</div>
						<div class="panel-body">
							<form action="index.php" method="GET">
								<input type="submit" value="Choose Red"/>
							</form>
						</div>
					</div>
				</div>
				<div class="col-md-6">
					<div class="panel panel-primary" style="margin-top:50px">
						<div class="panel-heading">
							<h3 class="panel-title" style="color:blue">Blue</h3>
						</div>
						<div class="panel-body">
							<form action="index.php" method="POST">
								<input type="submit" value="Choose Blue"/>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>
```

In here we can see that apparenty you can change the background color of the webpage using html-forms to send different requests. <br/>
The important thing to notice here is that for each color change a different `HTTP method` is being used. <br/>
Seeing this we can use a tool like `nikto` to scan for abnormal `HTTP method` types. <br/>
```sh
$ nikto -h http://mercury.picoctf.net:28916/index.php

nikto -h http://mercury.picoctf.net:28916/index.php

- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          18.189.209.142
+ Target Hostname:    mercury.picoctf.net
+ Target Port:        28916
+ Start Time:         2024-02-21 07:47:54 (GMT1)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Uncommon header 'flag' found, with contents: picoCTF{r3j3ct_th3_du4l1ty_70bc61c4}
```

Running `nikto` on the website we are able to find the flag which concludes this writeup. 