from random import sample

vector = sample(list(range(0, 100)), 10)

def check_value(vector, value):
    
    if(value == vector[0]):
        return True
    
    if(len(vector) == 1):
        return False

    return check_value(vector[1:], value)

print(check_value(vector, 1))