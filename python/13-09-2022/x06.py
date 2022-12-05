def mdc(x, y):
    if(y <= x and x%y == 0):
        return y
    
    if(x<y):
        return mdc(y, x)
    
    return mdc(y, x%y)

print(mdc(10, 5))