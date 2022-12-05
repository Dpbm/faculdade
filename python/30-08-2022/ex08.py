from ex07.valid_date import valid_date
from datetime import date

b_day, b_month, b_year = [ int(i) for i in input("Birth [DD/MM/YYYY]: ").split('/')]

if(not valid_date(b_year, b_month, b_day)):
    print("Invalid date")
    sys.exit(1)

_, _, a_year = [ int(i) for i in date.today().strftime("%d/%m/%Y").split('/')]


total_years  = a_year - b_year


print(f"this person is {total_years} years old")

