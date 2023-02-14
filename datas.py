from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def ManipulacaoDataHora():
    dias = ["seg","ter","qua","qui","sex","sab","dom"]
    hoje = date.today()
    print("Hoje é:", hoje)
    print("Partes da data:",hoje.day,hoje.month,hoje.year)
    print("Número do dia da semana:",hoje.weekday())
    print("Abreviação dia semana:",dias[hoje.weekday()])

    data = datetime.now()
    print("Data e hora de hoje:",data)

    tempo = datetime.time(data)
    print("Hora atual:",tempo)

ManipulacaoDataHora()    


##FORMATAÇÃO DE DATA
# %y = 23                   %Y=2023 
# %a=seg                    %A=SEGUNDA 
# %b=fevereiro              %B=fev             %m = 2
# %d=dia do mes             %c= data e hora da localidade
# %x= data da localidade    %X= hora da localidade

##FORMATAÇÃO DE HORA
# %I/%H = 12/24Hrs     
# %M = MINUTO
# %S = SEGUNDO
# %p = AM/PM

def formataDataHora():
    hoje = datetime.now()

    print(hoje.strftime("O ano é %d/%b/%Y"))
    print(hoje.strftime("Data e hora local: %c"))
    print(hoje.strftime("Hora atual -> %I:%H %p"))

formataDataHora()


def deltaTempo():
    delta = timedelta(days = 86, hours= 8532, minutes=7645)
    print(delta)

    hoje = datetime.now()

    print("Data no futuro:",hoje + delta)
    print("Data no passado:",hoje - delta)

deltaTempo()


def quantosDiasFaltam(ano, mes, dia):
    hoje = date.today()
    dataProcurada = date(ano,mes,dia)

    qtsDias = dataProcurada - hoje

    mensagem = "Faltam " + str(qtsDias).replace("days, 0:00:00", "") + "dias para a data " + dataProcurada.strftime("%d/%m/%Y")

    print(mensagem)

quantosDiasFaltam(2024,2,13)