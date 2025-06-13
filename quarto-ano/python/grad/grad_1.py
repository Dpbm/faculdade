import numpy as np
import matplotlib.pyplot as plt

def f(a,b):
    return 2*a + b**2

x = np.arange(0,10)
y = np.arange(0,10)

vec_f = np.vectorize(f)
z = vec_f(x,y)

def grad_f(b):
    return (2, 2*b)

vec_grad_f = np.vectorize(grad_f)
u, v  = vec_grad_f(y)

ax = plt.figure().add_subplot(projection='3d')
ax.scatter(x,y,z,marker="x",c='r')
ax.quiver(x, y, z, u, v, np.zeros_like(u))
plt.show()