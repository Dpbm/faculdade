def comb(n, k):
    if(k == 1):
        return n
    
    if(k == n):
        return 1
    
    return comb(n-1, k-1) + comb(n-1, k)


print(comb(4, 3))