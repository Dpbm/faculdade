import sys

try:
    stack = [None, None, None, None]
    pointer = 0
    print("Comands: ")
    while True:
        inp = input().split()
        command = inp[0]

        if(command == 'PUSH'):

            if(pointer == 0 and stack[pointer] is not None):
                raise Exception('STACK OVERFLOW')

            data = inp[1]
            stack[pointer] = data
            pointer = (pointer+1)%4

        elif(command == 'POP'):

            if(pointer == 0 and stack[pointer] is None):
                raise Exception('STACK UNDERFLOW')

            pointer = (pointer-1)%4
            stack[pointer] = None

        elif(command == 'SHOW'):
            print('\n'+('-'*10)+'\n')
            for index, value in enumerate(reversed(stack)):
                print(f'{-1*(index-3)} - {value}')
            print('\n'+('-'*10)+'\n')
        else:
            print("INVALID")
except Exception as error:
    print(error)
    sys.exit(1)
