from random import sample

biggest = lambda l : (max(l),  l.index(max(l)))


random_list = sample(list(range(1, 50)), 10)

first_biggest_value, first_biggest_value_index = biggest(random_list)
random_list[first_biggest_value_index] = 0
second_biggest_value, second_biggest_value_index = biggest(random_list)

print(f"Primeiro maior valor: {first_biggest_value} i{first_biggest_value_index}")
print(f"Segundo  maior valor: {second_biggest_value} i{second_biggest_value_index}")
