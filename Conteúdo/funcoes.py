def funcao():
    print('Hello World')


def calcularSoma(A , B):
    return A + B

soma = calcularSoma(2,3)
print(soma)

def condicional(x):
    y = x * 3
    if(y >=3):
        print('É maior que 3, ' + str(y))
    elif (y==x):
        print('É igual a ' + str(x))
    else:
        print('É menor que 3, ' + str(y))


def funcFor():
    for x in range(5,10):
        print(x)


funcFor()

def forArray():
    dias = ["segunda","terca","quarta","quinta","sexta","sabado","domingo"]
    for d in dias:
        print(d)

forArray()

def forArrayEnumerated():
    dias = ["segunda","terca","quarta","quinta","sexta","sabado","domingo"]
    for i, d in enumerate(dias):
        print(i,d)

forArrayEnumerated()

def forEnumerated():
    dias = ["segunda","terca","quarta","quinta","sexta","sabado","domingo"]
    for i, d in enumerate(dias):
        print(i)

forEnumerated()

def loopBreak():
    for x in range(5,10):
        if (x == 7):
            print(str(x) + " é igual a 7")
            break
        print(str(x) + " é menor que 7")
    
loopBreak()

def loopContinue():
    for x in range(5,10):
        if (x == 7):
           continue
        print("o valor de x é " + str(x))
    
loopContinue()


