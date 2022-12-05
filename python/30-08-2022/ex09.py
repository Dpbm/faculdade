from ex07.valid_date import valid_date
import sys

months = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

date_text = lambda day, month, year : f"{day} de {months[month - 1].capitalize()} de {year}"

day, month, year = [ int(i) for i in input("Date [DD/MM/YYYY]: ").split('/')]

if(not valid_date(year, month, day)):
    print("Invalid date")
    sys.exit(1)

print(date_text(day, month, year))
