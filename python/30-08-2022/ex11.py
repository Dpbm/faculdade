def factorial(n):
    if(n == 1):
        return 1

    return n * factorial(n - 1)

sum_result_values = lambda values : sum([ int(i) for i in values ])
transform_result_into_list = lambda result : list(str(result))

print(sum_result_values(transform_result_into_list(factorial(int(input("value: "))))))