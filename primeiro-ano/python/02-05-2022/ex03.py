from random import sample, randint

def sort_list(non_sorted_list):
    if(len(non_sorted_list) < 1):
        return non_sorted_list

    pivot = non_sorted_list[0]

    middle = [i for i in non_sorted_list if i == pivot]

    left = [i for i in non_sorted_list if i < pivot]
    right = [i for i in non_sorted_list if i > pivot]

    return [*sort_list(left), *middle, *sort_list(right)]
    


A = sample(list(range(0, 50)), randint(1, 6))
B = sample(list(range(0, 50)), randint(1, 6))

all_lists = [*A, *B]

print(*A)
print(*B)
print(*sort_list(all_lists))
