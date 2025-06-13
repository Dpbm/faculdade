from math import cos, sin, pi

f_x = lambda x : 2*cos(x) - 4*x 
f_dx = lambda x : -2*sin(x) - 4

previous_x = 0
current_x = pi
current_xi = 1

while(input() == "s"):
    f_x_result = f_x(current_x)
    f_dx_result = f_dx(current_x)
    result = current_x - (f_x_result/f_dx_result)

    result_formated = float(f'{result:.4f}')
    line = f"x{current_xi} = {current_x} - ({f_x_result}/{f_dx_result}) = {result_formated}"
    
    previous_x = current_x
    current_x = result_formated


    diff = abs(current_x - previous_x)
    print(line)
    print(f"diff = {diff}")

    if (diff == 0.0):
        print("Found")
        break


    current_xi += 1

