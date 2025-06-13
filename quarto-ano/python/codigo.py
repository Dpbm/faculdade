from abc import ABC, abstractmethod
import logging 
from datetime import datetime

class Banker(ABC):
    """Interface do banqueiro que define os métodos para depósito e saque.
    
    Esta classe abstrata estabelece a interface que tanto a implementação real 
    quanto o proxy devem seguir. Ela garante que ambos tenham os métodos 
    'deposit' e 'withdraw'.
    """
    
    @abstractmethod
    def deposit(self, account_id, amount):
        """Método abstrato para depósito de dinheiro em uma conta.
        
        Este método deve ser implementado nas classes concretas. Recebe como 
        parâmetros o ID da conta e o valor a ser depositado.
        """
        pass

    @abstractmethod
    def withdraw(self, account_id, amount):
        """Método abstrato para saque de dinheiro de uma conta.
        
        Este método deve ser implementado nas classes concretas. Recebe como 
        parâmetros o ID da conta e o valor a ser sacado, retornando o valor 
        sacado.
        """
        pass


class BankerImpl(Banker):
    """Implementação real da interface do banqueiro.
    
    Esta classe implementa os métodos definidos na interface 'Banker' e 
    realiza as operações reais de depósito e saque.
    """


    
    def deposit(self, account_id, amount):
        """Depósito de dinheiro na conta especificada.
        
        Implementação real do método de depósito. Exibe uma mensagem indicando 
        que o depósito foi realizado.
        """
        print(f"Depositando o valor {amount} na conta {account_id}")

    def withdraw(self, account_id, amount):
        """Saque de dinheiro da conta especificada.
        
        Implementação real do método de saque. Exibe uma mensagem indicando 
        que o saque foi realizado e retorna o valor sacado.
        """
        print(f"Sacando o valor {amount} da conta {account_id}")
        return amount


class BankerProxy(Banker):
    """Proxy que adiciona uma camada de segurança ao acessar o banqueiro real.
    
    Esta classe implementa a interface 'Banker' e atua como um intermediário 
    entre o cliente e a implementação real do banqueiro. Ela pode adicionar 
    funcionalidades como segurança, controle de acesso, ou cache antes de 
    delegar as chamadas ao objeto real.
    """
    
    def __init__(self):
        """Inicializa o proxy com uma instância da implementação real do 
        banqueiro.
        
        Cria um objeto 'BankerImpl' que será usado para realizar as operações 
        reais, enquanto o proxy adiciona camadas adicionais de lógica.
        """
        self._banker = BankerImpl()

        # adiciona uma instancia do logger para ser usado posteriormente nos depósitos
        self._logger = logging.getLogger("Banker")
        logging.basicConfig(filename='bank_transactions.log', encoding='utf-8', level=logging.INFO)
    
    def _log(self, amount, account_id, status):
        """
        Método usado para fazer o logging 
        dos saques
        """

        status_msg =  'Bem sucedido' if status else 'Mal sucedido'
        time = str(datetime.now())
        log_str = f"[Saque]\nhorário: {time}\nvalor: {amount}\nid: {account_id}\nstatus: {status_msg}"
        if status:
            self._logger.info(log_str)
            return

        self._logger.error(log_str)
    
    def deposit(self, account_id, amount):
        """Intercepta a chamada ao método de depósito, adicionando uma 
        verificação de segurança.
        
        Este método permite o depósito apenas se o usuário for autorizado. 
        Caso contrário, lança uma exceção indicando que o usuário não tem 
        permissão.
        """
        #Isso normalmente seria verificado com base no contexto real do usuário
        user_id = "banker"  
        if user_id == "banker":
            self._banker.deposit(account_id, amount)
        else:
            raise PermissionError("O usuário atual não está autorizado a depositar")

    def withdraw(self, account_id, amount):
        """Intercepta a chamada ao método de saque e delega a execução ao 
        objeto real.
        
        Este método não adiciona lógica extra antes de delegar ao objeto real, 
        mas poderia ser estendido para incluir funcionalidades como logging ou 
        validações adicionais.
        """

        # adicionando logica para caso mal sucedido
        MAX_WITHDRAW = 1000
        if amount > MAX_WITHDRAW:
            self._log(amount, account_id, False)
            raise ValueError("Valor ultrapassa o limite de R$1000.00")

        self._log(amount, account_id, True)


        return self._banker.withdraw(account_id, amount)


# Exemplo de uso
if __name__ == "__main__":
    # Cria uma instância do proxy em vez de acessar diretamente o BankerImpl
    proxy = BankerProxy()
    
    # Tentativa de depósito
    try:
        proxy.deposit("12345", 100)  # Apenas permitido se user_id for 'banker'
    except PermissionError as e:
        print(e)
    
    # Tentativa de saque
    print(proxy.withdraw("12345", 50))

    # TENTATIVA MAL SUCEDIDA DE SAQUE
    proxy.withdraw("12345", 1004)