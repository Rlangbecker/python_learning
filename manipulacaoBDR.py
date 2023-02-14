##Manipulação de banco de dados Relacional

import sqlite3

def manipulaDados(bancoDados, comando):
    conexao = sqlite3.connect(bancoDados)

    cursor = conexao.cursor
    cursor.execute(comando)
    conexao.commit()
    conexao.close()

def selecionaDados(bancoDados,comando):
    conexao = sqlite3.connect(bancoDados)
    
    cursor = conexao.cursor
    cursor.execute(comando)
    linhas = cursor.fetchall()

    for linha in linhas:
        print(linha)

def manipulacaoDados():
    comandoInsert = "INSERT INTO estados (nome_estado , sigla_estado , nome_capital) VALUES ('Rio grande do sul','RS','Porto Alegre')"
    pathDB = "C\\***********************"
    comandoSelect = "SELECT nome_estado, sigla_estado, nome_capital FROM estados"

    manipulaDados(pathDB,comandoInsert)
    selecionaDados(pathDB,comandoSelect)
    
manipulacaoDados()