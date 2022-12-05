from random import sample, randint
from time import time


def bubble_sort(non_sorted_list):
    initial = time()

    while True:
        swaps = 0

        for i in range(0, len(non_sorted_list) - 1):
            if(non_sorted_list[i+ 1] > non_sorted_list[i]):
                swaps += 1
                non_sorted_list[i], non_sorted_list[i + 1] = non_sorted_list[i + 1], non_sorted_list[i]

        if(swaps == 0):
            break
    final = time()
    return (non_sorted_list, initial, final, (final - initial))


def by_sort_method(non_sorted_list):

    initial = time()
    sorted_list = sorted(non_sorted_list) 
    final = time()

    return(
        sorted_list,
        initial, 
        final, 
        (final - initial)
    )                



A = sample(list(range(0, 10000)), 10000)

sorted_list_bubble_sort, initial_time_bubble_sort, final_time_bubble_sort, difference_bubble_sort = bubble_sort(A)
sorted_list_sorted, initial_time_sorted, final_time_sorted, difference_sorted = by_sort_method(A)

print('-'*20)
print('Bubble sort')
print(f'inicio --> {initial_time_bubble_sort}')
print(f'fim --> {final_time_bubble_sort}')
print(f'total --> {difference_bubble_sort}')

print()

print('-'*20)
print('Sorted')
print(f'inicio --> {initial_time_sorted}')
print(f'fim --> {final_time_sorted}')
print(f'total --> {difference_sorted}')