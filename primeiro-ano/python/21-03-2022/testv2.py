'''n1 = int(input("valor 1: "))
n2 = int(input("valor 2: "))

values = sorted([n1, n2], reverse=True)

length_larger = len(str(values[0]))

carry = 0

for i in range(length_larger, 0, -1):
    factor = 10 ** i
    carry += ((values[0] % factor) + (values[1] % factor)) // factor

print(f'{carry} carries')'''

BPF = 53        
RECIP_BPF = 2 ** -BPF

 print ((int.from_bytes(_urandom(7), 'big') >> 3) * RECIP_BPF)
