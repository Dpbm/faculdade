from ex07.valid_date import valid_date
import sys

day, month, year = [ int(i) for i in input("Date [DD/MM/YYYY]: ").split('/')]

if(not valid_date(year, month, day)):
    print("Invalid date")
    sys.exit(1)

print("It's a valid date!")

