L = [1, 3, 6]

def insert_sort(value):
    global L
    if(len(L) == 0):
        L.append(value)
        return
    
    elif (len(L) == 1):
        L.insert(value, 0 if L[0] > value else 1)
        return 

    elif (value > L[-1]):
        L.append(value)
        return

    elif (value < L[0]):
        L.insert(0, value)
        return
    
    index = old = len(L)
    partial_array = L

    while True:
        medium_point = len(partial_array) // 2


        if(value == partial_array[medium_point]):
            index = medium_point
            L.insert(index, value)
            print('ja no primeiro')
            break

        if(value > partial_array[medium_point]):
            index += len(partial_array[:medium_point])
            partial_array = partial_array[medium_point:]

            
            

        else:
            index -= len(partial_array[medium_point:])
            partial_array = partial_array[:medium_point + 1]
            

        if(old == len(partial_array)):
            print('saiu')
            break    

        old = len(partial_array)

    

    L.insert(index, value)
    print(L)


try:
    while True:
        insert_sort(int(input('valor: ')))

except KeyboardInterrupt:
    print(f'Os valores resultantes são --> {L}')

except Exception as error:
    print(error)
    exit()