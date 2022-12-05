value = int(input('valor: '))

def prime(value):
    prime_value = True
   
    if(-1 <= value <= 1):
        return False

    # vc nn precisa chegar ate o numero pois todo numero e divisivel 
    # apenas ate a metade dele (value // 2 + 1), tbm nao e necessario testar 
    # por 1, ja que todo numero e divisivel por 1

    for i in range(2, value//2 + 1):
        if(value % i == 0):
            prime_value = False


    return prime_value

def super_prime(value):
    #numeros que sao primos e sua posicao na lista tambem e um numero primo
    
    if(prime(value)):

        counter = 0
        for i in range(2, value + 1):
            if(prime(i)):
                counter += 1
        
        return prime(counter)

    else:
        return False
            


print(super_prime(value))


    
    