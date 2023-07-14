import sympy
import matplotlib.pyplot as plt

def integrand(t,x):
	return f(t)*g(x-t)

def f(x):
	return sympy.Piecewise((1,abs(x) <= 1), (0, True))

def g(x):
	return sympy.Piecewise(((1-x)/2,abs(x) <= 1), (0, True))

def convolution(u,x,a=10,d=0.1):
	# exp = (integrand(1/u - 1,x) + integrand(-1/u + 1,x)) * u ** -2
	s = 0
	for n in range(0,int(2*a/d)+1):
		s += integrand(n*d-a,x)*d
	return s

u,x=sympy.symbols('u,x')

xs = []
ys = []

x,u = sympy.symbols('x,u')
for i in range(0,1001):
	x = i / 100  - 5
	xs.append(x)
	ys.append(convolution(u,x).evalf())
	print(xs[-1],ys[-1])

plt.plot(xs,ys)
plt.axis([-5,5,-2,2])
plt.show()
