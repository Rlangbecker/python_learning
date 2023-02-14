f=0
print(f)

def funcao():
    f="funcao"
    print(f)


funcao()

print(f)

def funcaoGlobal():
    global f
    f="funcao global"
    print(f)


funcaoGlobal()
print(f)