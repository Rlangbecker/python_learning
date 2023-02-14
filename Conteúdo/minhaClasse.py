
class minhaClasse():
    def __init__(self):
        self.nome = "Ricardo"

    def calcularIdade(self,x):
        self.idade = 2023 - x
        print(str(self.idade)+" anos")

def criarInstancia():
    meuObjeto = minhaClasse()
    nome = meuObjeto.nome
    print(nome)
    
    minhaIdade = meuObjeto.calcularIdade(1994)
    print(minhaIdade)

criarInstancia()