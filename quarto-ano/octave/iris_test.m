pkg load io

data = csv2cell("iris.csv")

x1 = cell2mat(data(2:end,2))
x2 = cell2mat(data(2:end,4))

y = cell2mat(data(2:end,3))
z = cell2mat(data(2:end,5))

colors = []
labels = data(2:end,6)

for i = 1:length(labels)
  label = char(labels{i})
  color = 10

  if strcmp(label, "Iris-versicolor")
     color = 120
  elseif strcmp(label, "Iris-virginica")
     color = 60
  endif

   colors(end+1) = color
endfor


hold on

subplot(1,2,1)
scatter3(x1, y, z, 50, colors, "filled")
title({"comparison";...
       "SepalLengthCm x SepalWidthCm x PetalWidthCm"})
subplot(1,2,2)
scatter3(x2, y, z, 50, colors, "filled")
title({"comparison";...
       "PetalLengthCm x SepalWidthCm x PetalWidthCm"})

hold off




