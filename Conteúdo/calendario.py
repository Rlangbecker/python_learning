import calendar

def calendario():
    calendarioTexto = calendar.TextCalendar(calendar.SUNDAY)
    txtCalendario = calendarioTexto.formatyear(2023)
  #  txtCalendarioTESTE = calendarioTexto.formatmonth(2023,1)
    print(txtCalendario)
  #  print(txtCalendarioTESTE)

#calendario()


def calendarioHtml():
    calendarioHtml = calendar.HTMLCalendar(calendar.SUNDAY)
    htmlCalendario = calendarioHtml.formatyear(2023)
  #  txtCalendarioTESTE = calendarioTexto.formatmonth(2023,1)
    print(htmlCalendario)
  #  print(txtCalendarioTESTE)

#calendarioHtml()

def imprimiMes():
    for mes in calendar.month_name:
        print(mes)

   # for dia in calendar.day_name:
   #     print(dia)

imprimiMes()