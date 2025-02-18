from classes import Guerreiro, Mago, Arqueiro
from arma import Arma
from random import choice,randint

NAMES = ["Eloide", "Althea", "Skye", "Quinn", "Niahm", "Auron", "Jecht", "Zaon", "Baralai", "Balthier"]
WEAPONS = ["Katana", "Shotgun", "Sniper", "Excalibur", "Eclipse"]
classes = {
        "mago":Mago,
        "guerreiro":Guerreiro,
        "arqueiro":Arqueiro
    }

classes_names = list(classes.keys())

if __name__ == '__main__':
    first_class = choice(classes_names)
    second_class = choice(classes_names)

    first_name = choice(NAMES)
    second_name = choice(NAMES)

    life_p1 = randint(10, 100)
    life_p2 = randint(10, 100)

    min_attack_p1 = randint(10, 40)
    max_attack_p1 = randint(40, 60)

    min_attack_p2 = randint(10, 40)
    max_attack_p2 = randint(40, 60)

    p1 = classes[first_class](first_name, life_p1, min_attack_p1, max_attack_p1)
    p2 = classes[second_class](second_name, life_p2, min_attack_p2, max_attack_p2)

    if(randint(0,1)):
        weapon_p1 = choice(WEAPONS)
        p1.adicionar_arma(Arma(weapon_p1, randint(1,10)))
    if(randint(0,1)):
        weapon_p2 = choice(WEAPONS)
        p2.adicionar_arma(Arma(weapon_p2, randint(1,10)))

    print(p1)
    print("        Contra")
    print(p2)

    order = [p1, p2]
    get_current = lambda i:i%2
    get_next = lambda i: (i+1)%2
    to_attack = randint(0,1)


    print("\n\nE que comecem as batalhas", end="\n\n")

    while p1.esta_vivo() and p2.esta_vivo():
        attacking = order[get_current(to_attack)]


        type_of_attack = randint(0,1) # 0=standard, 1=special
        opponent = order[get_next(to_attack)]

        if(type_of_attack == 0):
            print(f"{attacking.nome} usou o ataque simples")
            attacking.atacar(opponent)
        else:
            print(f"{attacking.nome} usou o ataque especial")
            attacking.ataque_especial(opponent)
        
        print(opponent)
        print("="*30)

        to_attack+=1

    print(f"{p1.nome if p1.esta_vivo() else p2.nome} venceu a batalha !!!")
