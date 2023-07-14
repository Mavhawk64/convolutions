import sympy

def integrand(t,x):
	return f(t)*g(x-t)

def convolution(u,x):
	return sympy.integrate((integrand(1/u - 1,x) + integrand(-1/u + 1,x)) * u ** -2,(u,0,1))

def f(x):
	return sympy.Piecewise((1,abs(x) <= 1), (0, True))

def g(x):
	return sympy.Piecewise(((1-x)/2,abs(x) <= 1), (0, True))

x, u = sympy.symbols('x,u')
for i in range(0,100):
	x = i / 50 - 1
	print(convolution(u,x).evalf())