
from html.parser import HTMLParser

class meuParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs):
        print("tag de abertura encontrada")
        if attrs.__len__() > 0 :
            for a in attrs:
                print("Valores encontrados: ", a[0]," - ",a[1])

    def handle_endtag(self, tag):
        print("Tag de fechamento encontrada")


    def handle_comment(self, data):
        print("comentario encontrando")

    def handle_data(self,data):
        print("Valores encontrados")
        if data.isspace():
            print("Valor encontrado é um espaço")
        else:
            print("O valor encontrado foi: ",data)
            

def meuObjeto():
    meuParser1 = meuParser()
    arquivo = open("C:\\Users\\ricardo.langbecker\\Desktop\\calendario.html","r")
    dados = arquivo.read()

    meuParser1.feed(dados)

meuObjeto()