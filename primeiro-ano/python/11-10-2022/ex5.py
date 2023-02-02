get_digits       = lambda digit: list(map(int, list(str(digit))))
get_digits_sum   = lambda digits: sum(digits)
get_digits_len   = lambda digits: len(digits)
get_digits_mean  = lambda n_digits, sum_digits: sum_digits / n_digits
  
digit = int(input())

digits     = get_digits(digit)
sum_digits = get_digits_sum(digits)
n_digits   = get_digits_len(digits) 

print(get_digits_mean(n_digits, sum_digits))
