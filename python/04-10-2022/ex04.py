a = {
    "t":1,
    "d":3,
    "c":4,
    "v":12
}

print(a.get('t', "deu bosta"))
print(a.get('td', "deu bosta"))
print(a.pop("t", "deu merda"))
print(a.pop("td", "deu merda"))
print(a)