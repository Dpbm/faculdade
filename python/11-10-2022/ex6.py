from random import randint
from collections import Counter

launch_die           = lambda   : randint(1, 6)
launch_die_n_times   = lambda n : [launch_die() for _ in range(n)]
count_launch_results = lambda results : dict(Counter(results))  
get_a_launch_result  = lambda results, number : results[number]
show_result          = lambda result, number : print(f'{number} saiu {result} vezes')      

results         = launch_die_n_times(100)
counted_results = count_launch_results(results)

for i in range(1, 7):
    show_result(get_a_launch_result(counted_results, i), i)