b = 3
a = 9


last =  1
for i in range(100):
    xi = (1/b) * ((b-1)*last + (a/(last**(b-1))))
    print(xi)
    last = xi
