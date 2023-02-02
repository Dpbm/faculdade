N = 9


def store_array(n=0, array=[]):
    if(n == N):
        return array

    return store_array(n + 1, [*array, int(input(f"Valor {n}: "))])

def print_array(array):
    if(not len(array)):
        return
    
    print(array[0], end=" ")
    print_array(array[1:])

print_array(store_array())