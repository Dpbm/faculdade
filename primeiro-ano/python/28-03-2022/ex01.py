

def fibonacci(last, current, counter, max_counter):
    print(last + current)

    if(counter < max_counter) :
        fibonacci(current, last + current, counter + 1, max_counter)



fibonacci(1, 0, 1, 100)