BLUE = '\033[94m'
GREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

main_menu = lambda: int(input("""
1. Adminsitrador
2. Participante
0. Sair
"""))

first_option = lambda: int(input("""
1. Listar
2. Consultar
3. Gerar Sorteio
0. Voltar
"""))

second_option = lambda : int(input("""
1. Cadastrar
2. Consultar Amigo Secreto
0. Sair
"""))

def user_already_exists(name):
    try:
        participants = open('participants.txt', 'r')

        data = set([ participant.replace('\n', '').split(';')[0] for participant in participants.readlines()])

        participants.close()

        return name in data

    except FileNotFoundError:
        return False

def get_password():
    default_password = '123456'
    attemps = 3
    correct_password = False
    from getpass import getpass
    while attemps and not correct_password:
        password = getpass("Senha: ")
        
        correct_password = password == default_password

        if(not correct_password):
            print(f"{FAIL}Senha inválida{ENDC}")
            print(f"{WARNING}{attemps - 1} tentativas restantes{ENDC}\n")
    
        attemps -= 1

    if(not correct_password):
        print(f"{FAIL}Você digitou a senha 3 vezes errada{ENDC}")
        print(f"{GREEN}Por favor, tente novamente mais tarde{ENDC}")
        exit()

def list_participants():
    try:
        participants = open('participants.txt', 'r')

        print(f"{BLUE}Dados dos participantes{ENDC}")
    
        data = [ participant.replace('\n', '').split(';') for participant in participants.readlines()]

        if(not len(data)):
            print(f"{FAIL}Nenhum participante cadastrado!{ENDC}")
            return

        from tabulate import tabulate
        print(tabulate(data, headers=["Nome", "Email", "Senha", "Amigo Secreto"], tablefmt="rounded_outline"))
        
        participants.close()
    except FileNotFoundError:
        print(f"{FAIL}Nenhum participante cadastrado!{ENDC}")

def consult():
    try:
        participant = input("Nome do participante: ")

        participants = open('participants.txt', 'r')

        if(not user_already_exists(participant)): 
            print(f"{FAIL}O participante requerido não foi encontrado!{ENDC}")
            return
        participants.seek(0)
        data = participants.readlines()

        if(not len(data)): 
            print(f"{FAIL}Nenhum participante cadastrado!{ENDC}")
            return

        for participant_data in data:
            participant_data = participant_data.replace('\n', '')
            

            name = participant_data.split(';')[0]
          
            if(name == participant): 
                print(f"{GREEN}Participante Encontrado{ENDC}")
                participant_data = participant_data.split(';')

                from tabulate import tabulate
                print(tabulate([participant_data], headers=["Nome", "Email", "Senha", "Amigo Secreto"], tablefmt="rounded_outline"))
                break
        
        participants.close()
    except FileNotFoundError:
        print(f"{FAIL}Nenhum participante foi cadastrado!{ENDC}")

def generate_raffle():
    try:
        participants = open('participants.txt', 'r+')
        participants_data = participants.readlines()
        raffle = []

        if(len(participants_data) <= 2):
            print(f"{FAIL}Quantidade insuficiente de participantes (necessario ao minimo 3 participantes){ENDC}")
            return

        names = [
            data.split(';')[0]
            for data in participants_data
        ]

        for data in participants_data:
            participant_data = data.split(';')
            participant_name = participant_data[0]
            selected_name = names[0]
            participant_name_index = names.index(participant_name)
            if(participant_name_index != len(names) - 1): selected_name = names[participant_name_index + 1]
            
            if(len(participant_data) >= 4):
                raffle.append(f'{";".join(participant_data[:3])};{selected_name}\n')
            else:
                raffle.append(data.replace('\n', '') + f';{selected_name}\n')
                

        participants.seek(0)
        participants.writelines(raffle)
        participants.close()
    except FileNotFoundError:
        print(f"{FAIL}Nenhum participante foi cadastrado!{ENDC}")

def first_menu_wrapper():
    get_password()
    
    functions = {
        1: list_participants, 
        2: consult,
        3: generate_raffle,
        0: lambda : None
    }

    selected_function = 1

    while selected_function:
        selected_function = first_option()
        function = functions[selected_function]
        function()

def add_participant():
    print(f"{BLUE}Adicione um participante{ENDC}")

    import re
    from getpass import getpass

    email = password = name = ''
    valid_email = re.compile("^[\w+.]+@\w+\.\w{2,}(?:\.\w{2})?$")

    while not(valid_email.match(email)) or not(name) or not(password) or user_already_exists(name):
        name = input("nome: ")
        email = input("email: ")
        password = getpass("senha: ")
        if(not(valid_email.match(email)) or not(name) or not(password)): print(f"{FAIL}Valores inválidos!{ENDC}")
        elif(user_already_exists(name)): print(f"{FAIL}Esse participante já foi cadastrado!{ENDC}")
        print()

    participants = open("participants.txt", 'a')
    participants.writelines(f"{name};{email};{password}\n")
    participants.close()

def consult_secret_friend():
    try:
        attemps = 3
        correct_login = False

        participants = open('participants.txt', 'r')

        from getpass import getpass

        while attemps and not correct_login:
            name = input("nome: ")
            password = getpass('senha: ')

            participants.seek(0)

            if(name not in participants.read()): 
                print(f"{FAIL}O participante requerido não foi encontrado!{ENDC}")
                break

            participants.seek(0)
        
            data = participants.readlines()

            if(not len(data)): 
                print(f"{FAIL}Nenhum participante cadastrado!{ENDC}")
                break

            for participant_data in data:
                participant = participant_data.replace('\n','').split(';')
                participant_name = participant[0]
                participant_password = participant[2]

                if(participant_name == name and participant_password == password):
                    correct_login = True
                    try:
                        secret_friend = participant[3]
                        if(secret_friend): print(f"{GREEN}Seu amigo secreto é o(a): {secret_friend}{ENDC}")
                        else: print(f"{WARNING}O sorteio ainda não foi realizado!{ENDC}")
                        break
                    except:
                        print(f"{WARNING}O sorteio ainda não foi realizado!{ENDC}")
                        break
                        

            if(not correct_login):
                print(f"{FAIL}Nome e\ou senha inválido(s)!{ENDC}")
                print(f"{WARNING}{attemps - 1} tentativas restantes!{ENDC}")
                attemps -= 1 
                
        participants.close()
    except FileNotFoundError:
        print(f"{FAIL}Nenhum participante foi cadastrado!{ENDC}")

def seccond_menu_wrapper():
    selected_function = 1

    functions = {
        1: add_participant,
        2: consult_secret_friend,
        0: lambda : None
    }

    while selected_function:
        selected_function = second_option()
        function = functions[selected_function]
        function()


menus = {
    1: first_menu_wrapper,
    2: seccond_menu_wrapper,
    0: lambda : None
}


selected_menu = 1

while selected_menu:
    selected_menu = main_menu()
    menu = menus[selected_menu]
    menu()


