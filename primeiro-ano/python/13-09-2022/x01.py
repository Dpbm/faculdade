def sum_list(input_list):
    if(len(input_list) == 1):
        return input_list[0]
    return input_list[0] + sum_list(input_list[1:])

print(sum_list([1, 2, 3, 4, 5]))