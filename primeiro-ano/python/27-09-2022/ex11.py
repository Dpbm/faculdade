media_digitos = lambda n : sum([ int(i) for i in str(n) ]) / len(str(n))

n = 1000
print(media_digitos(n))