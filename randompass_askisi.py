import random
import string

def rand_pass():
    pass_library = list(string.ascii_letters + string.digits + string.punctuation)
    mhkos = int(input('Give pass length: '))
    if mhkos in range(8,17):
        passw = []
        for i in range(length):
            passw.append(random.choice(pass_library))
    else:
         print('not supported')
    return''.join(passw)

passwd = rand_pass()
print(passwd)
