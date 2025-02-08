import Plots: savefig,plot

function bisectionMethod(f, a, b, max_steps, precision)
	memo = IdDict()
	step = 1

	while step < max_steps
		xk = (a+b)/2

		f_a = get(memo, a, nothing)
		f_xk = get(memo, xk, nothing)

		if f_a == nothing
			f_a = f(a)
			memo = merge(memo, Dict(a => f_a))
		end

		if f_xk == nothing
			f_xk = f(xk)
			memo = merge(memo, Dict(xk => f_xk))
		end

		signal = f_a * f_xk
		error = b - a

		signal_desc = signal < 0 ? "negative" : "positive"

		println("step: ", step, "; a: ", a, "; b: ", b, "; xk: ", xk, "; signal: ", signal_desc, "; f(a): ", f_a, "; f(xk): ", f_xk, "; precision: ", error)

		if f_a == 0
			return a
		elseif f_xk == 0 || error <= precision
			return xk
		elseif signal > 0
			a = xk
		elseif signal < 0
			b = xk
		end

		step += 1
	end
end

function plot_graph(f)
	x = range(-6,6)
	y = [ f(i) for i in x ]
	p = plot(x,y)
	savefig(p, "function-plot.png")
end

# precision
ε = 0.001
f(x) = x^3 - 9*x + 3

plot_graph(f)

final_value = bisectionMethod(f,-1,2, 1000, ε)
println("Final value: ", final_value)


