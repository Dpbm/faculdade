from datetime import datetime

class Mensagem:
    def exibir(self):
        pass

class MensagemBasica(Mensagem):
    def exibir(self):
        return "Olá!"

class MensagemDecorator(Mensagem):
    def __init__(self, mensagem):
        self._mensagem = mensagem

    def exibir(self):
        return self._mensagem.exibir()
    
class MensagemComNome(MensagemDecorator):
    def __init__(self, mensagem, nome):
        super().__init__(mensagem) 
        self._nome = nome  

    def exibir(self):
        return f"{self._mensagem.exibir()} Meu nome é {self._nome}."

class MensagemComEmoji(MensagemDecorator):
    def __init__(self, mensagem, emoji):
        super().__init__(mensagem)  
        self._emoji = emoji 

    def exibir(self):
        return f"{self._mensagem.exibir()} {self._emoji}"
    
class MensagemComSaudacao(MensagemDecorator):
    def __init__(self, mensagem):
        super().__init__(mensagem)  

    def exibir(self):
        current_hour = datetime.now().hour
        greeting = "Boa noite!"

        if current_hour >= 0 and current_hour < 12: # de meia noite a meio dia
            greeting = "Bom dia!"
        elif current_hour < 18: # ate 18h da tarde
            greeting = "Boa tarde!"

        return f"{greeting}\n{self._mensagem.exibir()}"
    

if __name__ == "__main__":
    mensagem = MensagemBasica()
    
    mensagem = MensagemComNome(mensagem, "Alice")
    mensagem = MensagemComEmoji(mensagem, "😊")
    mensagem = MensagemComSaudacao(mensagem)
    
    print(mensagem.exibir())