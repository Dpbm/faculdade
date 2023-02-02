import sys

def double_factorial(n):
    if(n == 1):
        return 1

    return n * double_factorial(n - 2)

check_odd = lambda value: value % 2 != 0

value = int(input("value: "))

if(not check_odd(value)):
    print("this value is not odd")
    sys.exit(1)

print(double_factorial(value))