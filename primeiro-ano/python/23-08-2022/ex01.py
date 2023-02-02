import sys

firstDigit = lambda cpf : sum([
        int(digit) * (index + 1) for index, digit in enumerate(cpf[:9])
    ]) % 11

secondDigit = lambda cpf : sum([
        int(digit) * (9 - index) for index, digit in enumerate(cpf[:9])
    ]) % 11

getCorrectDigit = lambda digit: 0 if digit >= 10 else digit

def validateCPF(cpf) -> bool:
    first  = getCorrectDigit(firstDigit(cpf))
    second = getCorrectDigit(secondDigit(cpf))

    return f'{first}{second}' == cpf[9:]

cpf = input()

if(not cpf.isdigit()):
    print("Por favor, digite apenas números!")
    sys.exit(1)

if(len(cpf) != 11):
    print("Por favor, digite um CPF!")
    sys.exit(1)

isAValidCPF = validateCPF(cpf)

if(isAValidCPF):
    print("CPF válido!")
    sys.exit(0)

print("CPF INVÁLIDO!")
sys.exit(1)