import math

t = 1000
k1 = 365*2


first_year_classes = math.trunc(k1/7)
print("FY: ",first_year_classes)
works_first_year = first_year_classes*2
print("works: ", works_first_year)
print('-'*100)

second_year_classes = math.trunc((t-k1)/7)
print("SY: ",second_year_classes)
works_second_year = second_year_classes*3
print("works: ", works_second_year)

