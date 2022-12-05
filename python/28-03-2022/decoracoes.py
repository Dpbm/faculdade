def decorador(func):

    def fun():
        print('vuzimid a funcao')
        return func()

    return fun

@decorador
def hello_world():
    return '1' + '19'

print(hello_world())