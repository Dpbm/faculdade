a = int(input("a: "))
b = int(input("b: "))

on_final = 1

while b != 0:
    if(a%10 != b%10 and on_final):
        on_final = 0

    a //= 10
    b //= 10

print(bool(on_final))