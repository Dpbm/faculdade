class GerenciadorDeImpressao:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        print(f"[DEBUG]: instance is = {self.__instance}")

        self.fila = []

    def adicionar(self, documento):
        self.fila.append(documento)

    def mostrar(self):
        print(" ".join(self.fila))

instancia1 = GerenciadorDeImpressao()
instancia2 = GerenciadorDeImpressao()

instancia1.adicionar('test1')
instancia2.adicionar('test2')
instancia2.adicionar('test3')

print("INSTANCIA 1")
instancia1.mostrar()
print("INSTANCIA 2")
instancia2.mostrar()