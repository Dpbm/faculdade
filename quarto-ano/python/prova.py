from numpy import arange

def area(a,b,n,f):
    h = (b-a)/n
    s = sum([f(xk) for xk in arange(a+h,b,h)])
    return (h/2)*(f(a)+f(b)+(2*s))

f = lambda x : 1/(1+x)
print(f"\033[42mÁrea total: {area(0,3,6,f):.6f}\033[0m")