def is_prime(number):
    if(number == 2):
        return True

    if(number <= 1 or number % 2 == 0):
        return False

    is_a_prime_number = True


    for i in range(3, number, 2):
        if (number % i == 0):
            is_a_prime_number = False
            break

    return is_a_prime_number