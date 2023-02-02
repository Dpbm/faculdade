C = int(input())

total = []

for i in range(C):
    values = [int(i) for i in input().split()]
    if(values[0] > len(values) -1):
        exit()

    total.append(values)



for list_of_means in total:
    class_average =  sum(list_of_means[1:]) / list_of_means[0] 
    total_of_mean_higher = [i for i in list_of_means if i > class_average]
    total_of_mean_higher_to_percentage = len(total_of_mean_higher) * 100 / list_of_means[0] 
    print(f'{total_of_mean_higher_to_percentage:.3f}%')

