f(x) = x^3 + 3*x - 1
g_xk(a,b) = (a+b)/2
e(a,b) = b-a

ε = 0.001

xk = 0
a = 0
b = 1
i = 0
error = e(a,b)

while error >= ε
    global xk = g_xk(a, b)
    f_a = f(a)
    f_xk = f(xk)
    signal = (f_a * f_xk) > 0 ? 1 : -1
    global error = e(a, b)

    if f_a == 0
        break
    elseif signal == 1
        global a = xk
    elseif signal == -1
        global b = xk
    end

    global i += 1
end

println("root: ", xk)