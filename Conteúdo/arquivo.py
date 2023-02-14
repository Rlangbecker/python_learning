
# w -> escrever arquivo  + -> se não existir, deve ser criado
#  \r\n   -> pula linha

def criarArquivo():
    arquivo = open("novoArquivo.txt","w+")

    arquivo.write("Linha gerada por python -> funcao criarArquivo \r\n")

    arquivo.close()

#criarArquivo()

# a -> apend .. escreva nas proximas linha

def editarArquivo():
    arquivo = open("novoArquivo.txt","a+")

    arquivo.write("Linha gerada por python -> funcao editarArquivo \r\n")

    arquivo.close()

#editarArquivo()


# r -> leitura
def lerArquivo():
    arquivo = open("novoArquivo.txt","r")
    if(arquivo.mode == "r"):
        conteudo = arquivo.read()
        print(conteudo)
    
    arquivo.close()

#lerArquivo()

def lerArquivoGrande():
    arquivo = open("novoArquivo.txt","r")
    if(arquivo.mode == "r"):
        conteudoTotal = arquivo.readlines()
    
    for linha in conteudoTotal:
        print(linha)
    
    arquivo.close()

#lerArquivoGrande()


#####################################################################################
#LEITURA DE ARQUIVOS

from os import path
import time


def dadosArquivo():
    ArquivoExiste = path.exists("novoArquivo.txt")
    ehDiretorio = path.isdir("novoArquivo.txt")
    pathArquivo = path.realpath("novoArquivo.txt")
    pathRelativo = path.relpath("novoArquivo.txt")
    dataCriacao = time.ctime(path.getctime("novoArquivo.txt"))
    dataModificacao = time.ctime(path.getmtime("novoArquivo.txt"))

    print(ArquivoExiste)
    print(ehDiretorio)
    print(pathArquivo)
    print(pathRelativo)
    print(dataCriacao)
    print(dataModificacao)

#dadosArquivo()


###########################################################################################
# MANIPULACAO DE ARQUIVOS

import os
from os import path
import shutil

def copiaArquivo():
    if path.exists("novoArquivo.txt"):
        pathArquivo = path.realpath("novoArquivo.txt")
        novoArquivo = pathArquivo + ".bkp"
        shutil.copy(pathArquivo,novoArquivo)

    #copiando permissoes
        shutil.copystat(pathArquivo,novoArquivo)

#copiaArquivo()

def renomearArquivo():
    if path.exists("novoArquivo.txt.bkp"):
        os.rename("novoArquivo.txt.bkp","BKP_novoArquivo.txt")

#renomearArquivo()


###################################################################
# COMPACTANDO ARQUIVOS

from shutil import make_archive
from zipfile import ZipFile

def criarZip1():
    shutil.make_archive("arquivoComp","zip","C:\\Variaveis\\Raspagem de dados\\FIAT")

#criarZip1()

def criarZip2():
    with ZipFile("ArquivoComp2.zip","w") as novoZip:
        novoZip.write("BKP_novoArquivo.txt")
        novoZip.write("novoArquivo.txt")
        novoZip.write("arquivoComp.zip")

#criarZip2()


def apagarArquivo():
    os.remove("arquivoComp.zip")

apagarArquivo()