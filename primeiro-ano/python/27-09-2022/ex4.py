from random import sample

l = sample(list(range(1, 50)), 20)

print(f"maior valor {max(l)}")
print(f"menor valor {min(l)}")
print(f"media dos valores {sum(l)/len(l)}")