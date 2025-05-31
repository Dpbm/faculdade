x = 0:50;

x_2 = @(x) 2*x;
x_3 = @(x) 3*x;

y1 = arrayfun(x_2, x);
y2 = arrayfun(x_3, x);

plot(x,y1,'o','MarkerSize', 8, 'MarkerEdgeColor', 'b', 'MarkerFaceColor', 'b');
hold on;

plot(x,y2,'o','MarkerSize', 8, 'MarkerEdgeColor', 'r', 'MarkerFaceColor', 'r');
hold on;

xs = cat(2,x,x);
ys = cat(2,y1,y2);

xs_sum = sum(xs);
ys_sum = sum(ys);

x_squared_fun = @(x) x^2;
xs_squared_sum = sum(arrayfun(x_squared_fun, xs));

x_y_fun = @(x,y) x*y;
x_y_sum = sum(arrayfun(x_y_fun, xs, ys));

n  = length(xs);

first_row = -1*n*xs_squared_sum;
second_row = xs_sum*xs_sum;

first_result = -1*n*x_y_sum;
second_result = xs_sum*ys_sum;

a = (first_result-second_result)/(first_row - second_row);
b = (ys_sum - (a*xs_sum))/n;

linear_fun = @(a,b,x) a*x + b;
approximated_values = arrayfun(linear_fun, a,b,x);

plot(x, approximated_values, '-', 'LineWidth', 2, 'Color', 'c');
hold on;


xs_to_pred = [1.5, 4.5, 3.3, 2.3, 1.1, 4.2, 5.4, 3.1];
ys_to_pred = [3, 9, 9.9, 6.9, 2.2, 12.6, 10.8, 9.3];

for i = 0:length(xs_to_pred)-1
  x_test = xs_to_pred(i+1)
  y_test = ys_to_pred(i+1)
  ref = linear_fun(a,b,x_test)
  color = 'b';
  if y_test > ref
    color = 'r';
  endif
  plot(x_test, y_test,'h','MarkerSize', 20, 'MarkerEdgeColor', color, 'MarkerFaceColor', color);
  hold on;
endfor


grid on;

title("Separate linear data");
legend("2x", "3x");
