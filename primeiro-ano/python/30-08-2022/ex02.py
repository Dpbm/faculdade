import sys
from functools import reduce

def power(base, exp):
    total_nums = [base]*exp
    return reduce((lambda x,y:x*y), total_nums)

base = int(input("base: "))
exp  = int(input("exp : "))

if(exp < 0):
    print("error, invalid exp!")
    sys.exit(1)

print(power(base, exp))
