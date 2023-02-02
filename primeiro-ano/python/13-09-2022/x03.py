# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ....
# 8, 5, 

"""
    value = 4 return 3
        value = 3 return 2
        value = 2 return 1



"""



def fibonacci(value):

    if (value <= 1):
        return value

    return fibonacci(value - 1) + fibonacci(value - 2)

print(fibonacci(10))