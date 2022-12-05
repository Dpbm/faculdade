value = int(input('valor: '))

def prime(value):
    prime_value = True
   
    if(-1 <= value <= 1):
        return 'not prime'

    # vc nn precisa chegar ate o numero pois todo numero e divisivel 
    # apenas ate a metade dele (value // 2 + 1), tbm nao e necessario testar 
    # por 1, ja que todo numero e divisivel por 1
    
    for i in range(2, value//2 + 1):
        if(value % i == 0):
            prime_value = False


    if(prime_value):
        return "it's prime"
    else:
        return 'not prime'


print(prime(value))


    
    