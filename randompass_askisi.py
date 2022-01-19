'''
ftiakse ena function to opoio tha zitaei apo ton xristi na dwsei mikos tou password me euros apo 8 eos 16 psifia
an o xristis dwsei timi alli apo auto to euros tha tou bgazei mnm oti den upostirizetai.
sti sunexeia to function tha kanei generate ena password to opoio tha exei mikos to mikos pou edwse o xristis
kai tha periexei toulaxiston 1 gramma ena symbolo kai 1 arithmo kai episis ena kefalaio gramma
telos tha kanei return ton kwdiko se mia metabliti me onoma passwd tin opoia kai tha kanei print ston xristi

BONUS
ean thes boreis na to ftiakseis etsi oste na zitaei apo ton xristi site gia to opoio kanei generate to password
kai na gurnaei sto telos ena dictionary me key to site kai value to password
BONUS 2
ean theleis boreis na to ftiakseis etsi oste an o xristis den dwsei timi eurous na kanei default sta 8 psifia
HINT
An thes boreis na to ulopoiiseis xrisimopoiontas to string module gia pio eukola. https://docs.python.org/3/library/string.html
'''

import random
import string

def rand_pass():
    pass_library = list(string.ascii_letters + string.digits + string.punctuation)
    mhkos = int(input('Dwse mhkos kwdikou: '))
    if mhkos in range(8,17):
        passw = []
        for i in range(mhkos):
            passw.append(random.choice(pass_library))
    else:
         print('Den yposthrizetai')
    return''.join(passw)

passwd = rand_pass()
print(passwd)
