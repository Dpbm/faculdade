from itertools import product 


def crackPass(password):
    attemps = 0
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    for combination in product(letters, letters, letters):
        actualPass = "".join(combination)

        attemps += 1

        if(actualPass == password): 
            break

    return attemps




correct = lambda password : len(password) == 3 and password.isupper() and password.isalpha() 

password = ''

while not correct(password):
    password = input("Senha do cofre (3 letras maíusculas): ")

print("\nQUEBRANDO SENHA...\n")
attemps = crackPass(password)
print(f"A senha foi encontrada depois de {attemps} tentativa(s)")





