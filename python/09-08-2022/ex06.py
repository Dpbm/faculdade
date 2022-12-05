getMiddleOdd  = lambda a : a[(len(a) - 1) // 2]
getMiddleEven = lambda a : a[ (len(a) - 1) // 2 : ((len(a) - 1) // 2) + 2 ] 

def getFunction(t):
    if(len(t) % 2 == 0):
        return getMiddleEven
    
    return getMiddleOdd


text = input("Texto: ")

func = getFunction(text)

print( func(text) )
