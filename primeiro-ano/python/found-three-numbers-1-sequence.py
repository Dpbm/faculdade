inp = input()
total = 0
count = 0

for value in inp:
    if(value == '1'):
        count += 1
    else:
        count = 0
    
    if(count >= 3):
        total += 1

print(total)
