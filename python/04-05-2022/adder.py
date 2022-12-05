def add(a, b, carry):
  total_sum = a ^ b ^ carry
  new_carry = (a & b) | (b & carry) | (a & carry)

  return (total_sum, new_carry)


def make_operation(numbers):
    if (len(numbers) <= 1):
        return numbers[0]

    total = ''

    first_number = [int(i) for i in numbers[0]]
    second_number = [int(i) for i in numbers[1]] 

    if(len(first_number) > len(second_number)):
        pad = [0]*(len(first_number) - len(second_number))
        second_number = [*pad, *second_number]

    elif(len(first_number) < len(second_number)):
        pad = [0]*(len(second_number) - len(first_number))
        first_number = [*pad, *first_number]

    carry = 0
    for i in range(len(first_number) - 1, -1, -1):
        result, carry = add(first_number[i], second_number[i], carry)

        total = str(result) + total

    total = str(carry) + total if carry else total

    new_numbers = [total, *numbers[2:]]

    return make_operation(new_numbers)


numbers_to_sum = input('numbers: ').split()

if(len(numbers_to_sum) < 2):
  print("You need to provide two binary numbers at least")
  exit(1)

total = make_operation(numbers_to_sum)
print(f'result {total}')
  