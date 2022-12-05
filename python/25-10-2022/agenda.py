telephones = {}

person_exists = lambda name: telephones.get(name, None)
number_already_exists = lambda telephones, telephone: telephone in telephones
invalid_phones_input = lambda telephones: len(set(telephones)) != len(telephones)

def incluirNovoNome(name, person_telephones):
    if(person_exists(name)):
        return "Nome já foi inserido anteriormente"


    if(invalid_phones_input(person_telephones)):
        return "número repetidos"

    telephones[name] = person_telephones
    return "telefone adicionado"

def incluirTelefone(name, person_telephone):
    if(
        not person_exists(name) and 
        input("Deseja inserir o novo nome? ").lower() != 's'
    ):
        return "Nome não adicionado!"


    if(number_already_exists(telephones[name], person_telephone)):
        return "Número já existe na lista"

    telephones[name].append(person_telephone)

    return "Novo número adicionado!"

def excluirTelefone(name, person_telephone):
    if(not  person_exists(name)):
        return "Pessoa inexistente na agenda"
    
    if(not number_already_exists(telephones[name], person_telephone)):
        return "Essa pessoa não possui este número"

    if(len(telephones[name]) <= 0):
        del telephones[name]
        return "Pessoa removida da agenda"

    telephones[name].pop(person_telephone)

    return "Número removido"

def excluirNome(name):
    if(not person_exists(name)):
        return "Esse nome não existe na agenda"

    del telephones[name]
    
    return "Nome removido da agenda"       

def consultarTelefone(name):
    if(not person_exists(name)):
        return "Este nome não está na agenda"

    return f"telefones de {name}: {', '.join(telephones[name])}"


actions = [
    lambda : incluirNovoNome(input("Nome da pessoa: "), input("Números dela: ").split()),
    lambda : incluirTelefone(input("Nome da pessoa: "), input("Novo telefone: ")),
    lambda : excluirTelefone(input("Nome da pessoa: "), input("Telefone: ")),
    lambda : excluirNome(input("Nome da pessoa: ")),
    lambda : consultarTelefone(input("Nome da pessoa: ")),
    lambda : exit()
]

while True:
    action = int(input(
        """Ações disponíveis
            [0] incluir novo nome
            [1] incluir novo telefone para um nome existente
            [2] excluir telefone de uma pessoa existente na agenda
            [3] excluir nome da agenda
            [4] consultar telefones na agenda
                
            [5] SAIR"""
        ))

    command = actions[action]
    status = command()
    print(status)