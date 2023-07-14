import sympy
import matplotlib.pyplot as plt

def integrand(t,x):
	return f(t)*g(x-t)

def f(x):
	return sympy.Piecewise((1,abs(x) <= 1), (0, True))

def g(x):
	return sympy.Piecewise(((1-x)/2,abs(x) <= 1), (0, True))

def convolution(u,x):
	exp = (integrand(1/u - 1,x) + integrand(-1/u + 1,x)) * u ** -2
	summed = 0
	for i in range(0,len(X)):
		summed += W[i] * exp.evalf(subs={u:X[i]})
	return summed

X = [-0.991455371120813,-0.949107912342759, -0.864864423359769, -0.741531185599394, -0.586087235467691, -0.405845151377397, -0.207784955007898, 0, 0.207784955007898, 0.405845151377397, 0.586087235467691, 0.741531185599394, 0.864864423359769, 0.949107912342759, 0.991455371120813]
W = [0.022935322010529, 0.063092092629979, 0.104790010322250, 0.140653259715525, 0.169004726639267, 0.190350578064785, 0.204432940075298, 0.209482141084728, 0.204432940075298, 0.190350578064785, 0.169004726639267, 0.140653259715525, 0.10479001032225, 0.063092092629979, 0.022935322010529]

X = [(i + 1) / 2 for i in X]
W = [i / 2 for i in W]

# provided int(f(x),(x,0,1))
# ~ sum(i=0,n,w_i*f(x_i))
# x_i_scaled = (x_i + 1) / 2
# w_i_scaled = w_i / 2

xs = []
ys = []

x,u = sympy.symbols('x,u')
for i in range(0,101):
	x = i / 25 - 2
	xs.append(x)
	ys.append(convolution(u,x).evalf())
	print(xs[-1],ys[-1])

plt.plot(xs,ys)
plt.axis([-5,5,-2,2])
plt.show()
