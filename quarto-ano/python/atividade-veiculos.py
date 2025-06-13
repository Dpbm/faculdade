from abc import ABC, abstractmethod


# Produtos abstratos
class Veiculo(ABC):
    @abstractmethod
    def descrever(self):
        pass

class Motor(ABC):
    @abstractmethod
    def descrever(self):
        pass


# Produtos concretos
class Carro(Veiculo):
    def descrever(self):
        print("Carro é um véiculo terrestre")

class Aviao(Veiculo):
    def descrever(self):
        print("Avião é um veículo aéreo")

class Barco(Veiculo):
    def descrever(self):
        print("Barco é um veículo aquático")

class Combustao(Motor):
    def descrever(self):
        print("Esse veiculo usa um motor a combustão")

class Jato(Motor):
    def descrever(self):
        print("Esse veiculo usa um motor a jato")   

class Eletrico(Motor):
    def descrever(self):
        print("Esse veiculo usa um motor elétrico")   

# Fabrica abstrata
class FabricaVeiculos(ABC):
    @abstractmethod
    def criar_veiculo(self):
        pass

    @abstractmethod
    def criar_motor(self):
        pass

# Fabrica Concreta
class FabricaTerrestre(FabricaVeiculos):
    def criar_veiculo(self):
        return Carro()
    def criar_motor(self):
        return Combustao()
    
class FabricaAerea(FabricaVeiculos):
    def criar_veiculo(self):
        return Aviao()
    def criar_motor(self):
        return Jato()
    
class FabricaAquatica(FabricaVeiculos):
    def criar_veiculo(self):
        return Barco()
    def criar_motor(self):
        return Eletrico()
    

# Cliente
class Cliente:
    def criar_veiculo(self, tipo_veiculo):
        fabrica = None

        if(tipo_veiculo == "terrestre"):
            fabrica = FabricaTerrestre()
        elif(tipo_veiculo == "aereo"):
            fabrica = FabricaAerea()
        elif(tipo_veiculo == "aquatico"):
            fabrica = FabricaAquatica()
        else:
            raise ValueError("tipo de veiculo invalido")
        

        veiculo = fabrica.criar_veiculo()
        motor = fabrica.criar_motor()

        print(f"Foi criado um veiculo: {tipo_veiculo}")
        veiculo.descrever()
        motor.descrever()


if __name__ == "__main__":
    exit_program = False
    cliente = Cliente()

    while not exit_program:
        try:
            option = int(input("""
                    ====================
                    Criação de veículos:
                    [1] Terrestre
                    [2] Aéreo
                    [3] Aquático
                    [0] sair
                    ====================
                """))
            
            if option == 0:
                exit_program = True
            elif option == 1:
                cliente.criar_veiculo("terrestre")
            elif option == 2:
                cliente.criar_veiculo("aereo")
            elif option == 3:
                cliente.criar_veiculo("aquatico")
            else:
                print("Opção Inválida")
        except:
            exit()