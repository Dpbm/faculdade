
names    = input().split()
lengths  = list(map(len, names))
smallest = names[lengths.index(min(lengths))] 
print(names)
print(smallest)
