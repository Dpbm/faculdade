animals = {
    "vertebrado":{
        "ave":{
            "carnivoro": "aguia",
            "onivoro": "pomba"
        },
        "mamifero":{
            "onivoro": "homem",
            "herbivoro": "vaca"
        }
    },
    "invertebrado":{
        "inseto":{
            "hematofago":"pulga",
            "herbivoro":"lagarta"
        },
        "anelideo":{
            "hematofago":"sanguessuga",
            "onivoro":"minhoca"
        }
    }
}

structure = input()
category  = input()
feeding   = input()

print(animals[structure][category][feeding])