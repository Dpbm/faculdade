f_x = lambda x : x**7 - 1000
f_dx = lambda x : 7*(x**6)
error = 0.00000001

previous_x = 0
current_x = 1
current_xi = 1

while(input() == "s"):
    f_x_result = f_x(current_x)
    f_dx_result = f_dx(current_x)
    result = current_x - (f_x_result/f_dx_result)

    line = f"x{current_xi} = {current_x} - ({f_x_result}/{f_dx_result}) = {result}"
    
    previous_x = current_x
    current_x = result


    diff = abs(current_x - previous_x)
    print(line)
    print(f"diff = {diff}")

    if(diff < error):
        print("Found")
        break

    current_xi += 1

