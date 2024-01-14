# Emptiness

## Description
```
http://ctf.mf.grsu.by/tasks/023838760b034544becdb2d52f197ccd/
```

## Writeup

Looking at the sourcecode of the website we see something very interesting. <br/>
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Javascript - Source</title>

  <script>
    function login() {
      key = prompt('secret key');
      if ( key == 
grodno{2149c0vMGFf2Ug84gN3ndq4f9812} {
        alert('Вы ввели правильный секретный ключ.')
      }
      else {
        alert('Ошибка');
      }
    }
  </script>
</head>
  <body onload="login()">

  </body>
</html>
```

Obtaining the flag concludes this writeup. 