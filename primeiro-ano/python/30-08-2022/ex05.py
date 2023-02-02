from ex04.is_prime import is_prime

def generate_primes(range_primes):
    if(range_primes <= 1):
        return
    
    for i in range(2, range_primes):
        if(is_prime(i)):
            print(i, end=" ")

range_primes = int(input("number: "))
generate_primes(range_primes)