from abc import ABC, abstractmethod

class HamburgerBuilder(ABC):
    @abstractmethod
    def add_pao(self):
        pass

    @abstractmethod
    def add_carne(self):
        pass

    @abstractmethod
    def add_queijo(self):
        pass

    @abstractmethod
    def add_condimentos(self):
        pass

    @abstractmethod
    def add_cebola(self):
        pass

    @abstractmethod
    def get_result(self):
        pass


class Hamburger:
    def __init__(self):
        self.ingredientes = []

    def add_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def __str__(self):
        return f"Hamburger possui: {', '.join(self.ingredientes)}"


class ClassicHamburgerBuilder(HamburgerBuilder):
    def __init__(self):
        self.hamburger = Hamburger()

    def add_pao(self):
        self.hamburger.add_ingrediente("pão francês")
        return self

    def add_carne(self):
        self.hamburger.add_ingrediente("cordeiro")
        return self

    def add_queijo(self):
        self.hamburger.add_ingrediente("mussarela")
        return self

    def add_condimentos(self):
        self.hamburger.add_ingrediente("Maionese")
        return self
    
    def add_cebola(self):
        self.hamburger.add_ingrediente("cebola")
        return self

    def get_result(self):
        return self.hamburger

class CheeseburgerBuilder(HamburgerBuilder):
    def __init__(self):
        self.hamburger = Hamburger()

    def add_pao(self):
        self.hamburger.add_ingrediente("pão de forma")
        return self

    def add_carne(self):
        self.hamburger.add_ingrediente("carne de cabra")
        return self

    def add_queijo(self):
        self.hamburger.add_ingrediente("quejo brie")
        return self

    def add_condimentos(self):
        self.hamburger.add_ingrediente("molho especial")
        return self
    
    def add_cebola(self):
        self.hamburger.add_ingrediente("cebola roxa")
        return self

    def get_result(self):
        return self.hamburger

class VeggieBurgerBuilder(HamburgerBuilder):
    def __init__(self):
        self.hamburger = Hamburger()

    def add_pao(self):
        self.hamburger.add_ingrediente("pão de milho")
        return self

    def add_carne(self):
        self.hamburger.add_ingrediente("veggie burger")
        return self

    def add_queijo(self):
        self.hamburger.add_ingrediente("queijo vegano zero lactose")
        return self

    def add_condimentos(self):
        self.hamburger.add_ingrediente("folhas frescas com vinagre de limao vegano")
        return self

    def add_cebola(self):
        self.hamburger.add_ingrediente("cebola vegana")

    def get_result(self):
        return self.hamburger

class ChickenBurgerBuilder(HamburgerBuilder):
    def __init__(self):
        self.hamburger = Hamburger()

    def add_pao(self):
        self.hamburger.add_ingrediente("pão de alho")
        return self

    def add_carne(self):
        self.hamburger.add_ingrediente("peito de frango")
        return self

    def add_queijo(self):
        self.hamburger.add_ingrediente("queijo branco")
        return self

    def add_condimentos(self):
        self.hamburger.add_ingrediente("ketchup") 
        self.hamburger.add_ingrediente("mostarda")
        self.hamburger.add_ingrediente("maionese")
        self.hamburger.add_ingrediente("caldo de frango")
        return self
    
    def add_cebola(self):
        self.hamburger.add_ingrediente("cebola do himalaia")
        return self

    def get_result(self):
        return self.hamburger

class FishBurgerBuilder(HamburgerBuilder):
    def __init__(self):
        self.hamburger = Hamburger()

    def add_pao(self):
        self.hamburger.add_ingrediente("pão caseiro")
        return self

    def add_carne(self):
        self.hamburger.add_ingrediente("tilapia")
        return self

    def add_queijo(self):
        self.hamburger.add_ingrediente("gorgonzola")
        return self

    def add_condimentos(self):
        self.hamburger.add_ingrediente("branco")
        return self
    
    def add_cebola(self):
        self.hamburger.add_ingrediente("cebola aquatica")
        return self

    def get_result(self):
        return self.hamburger

class MaxBurgerBuilder(HamburgerBuilder):
    def __init__(self):
        self.hamburger = Hamburger()

    def add_pao(self):
        self.hamburger.add_ingrediente("3 pães brioche")
        return self

    def add_carne(self):
        self.hamburger.add_ingrediente("frango")
        self.hamburger.add_ingrediente("carne de vaca")
        self.hamburger.add_ingrediente("tilapia")
        self.hamburger.add_ingrediente("cabrito")
        self.hamburger.add_ingrediente("jacaré")
        return self

    def add_queijo(self):
        self.hamburger.add_ingrediente("gorgonzola com cheddar e mussarela")
        return self

    def add_condimentos(self):
        self.hamburger.add_ingrediente("molho branco")
        self.hamburger.add_ingrediente("molho de anchovas")
        return self
    
    def add_cebola(self):
        self.hamburger.add_ingrediente("cebola especial picante")
        return self

    def get_result(self):
        return self.hamburger
    
class Chef:
    def __init__(self, builder):
        self._builder = builder

    def get_hamburguer(self):
        return self._builder.add_pao().add_carne().add_queijo().add_condimentos().add_cebola().get_result()
    

if __name__ == "__main__":
    valid_options = list(range(7))
    builders = [
        ClassicHamburgerBuilder,
        CheeseburgerBuilder,
        VeggieBurgerBuilder,
        ChickenBurgerBuilder,
        FishBurgerBuilder,
        MaxBurgerBuilder
    ]


    while True:

        opcao = int(input(
            """
                1. Clássico
                2. Cheeseburger
                3. Vegetariano
                4. Frango
                5. Peixe
                6. Max Burger
                0. Sair
            """
        ))

        if opcao not in valid_options:
            print("opcao invalida!")
            continue

        if opcao == 0:
            break

        builder = builders[opcao - 1]
        chef = Chef(builder())
        hamburger = chef.get_hamburguer()
        print("Hamburguer criado: ")
        print(hamburger)