def prime(value):
    prime_value = True
   
    if(-1 <= value <= 1):
        return False
    
    for i in range(2, value//2 + 1):
        if(value % i == 0):
            prime_value = False


    return prime_value

def super_prime(value):
    is_a_super_prime = True

    for i in range(len(str(value)) - 1, 0, -1):
        actual = str(value)[:i]
        if(not prime(int(actual))):
            is_a_super_prime = False
            break

    return is_a_super_prime


N = int(input())

min_value = int('1' + (len('0' * (N - 1)) * '0'))
max_value = int('9' * len(N * '9'))

prime_numbers = []

for i in range(min_value, max_value):
    if(prime(i)):
        if(super_prime(i)):
            prime_numbers.append(i)

print(*prime_numbers)   
