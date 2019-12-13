#Метод Ньютона
import numpy as np

def F(x):
	y = np.zeros_like(x)
	y[0] = (3 + 2*x[0])*x[0] - 2*x[1] - 3
	y[1:-1] = (3 + 2*x[1:-1])*x[1:-1] - x[:-2] - 2*x[2:] -2
	y[-1] = (3 + 2*x[-1])*x[-1] - x[-2] - 4
	return y

def J(x):
	n = len(x)
	b = np.zeros((n, n))
	b[0, 0] = 3 + 4*x[0]
	b[0, 1] = -2
	for i in range(n-1):
		b[i, i-1] = -1
		b[i, i] = 3 + 4*x[i]
		b[i, i+1] = -2
	b[-1, -2] = -1
	b[-1, -1] = 3 + 4*x[-1]
	return b

def Sol(F, J, guess):
	N = len(guess)
	d = np.ones(N)
	x = np.array(guess, float)
	acc = 0.001
	k = 0
	while max(abs(d)) > acc and k < 100:
		d = np.linalg.solve(J(x), -F(x))
		x = x + d
		k += 1
	return x, k

n = 10
guess = 3*np.ones(n)
sol, its = Sol(F, J, guess)

if its > 0:
	print("x = {}".format(sol))
else:
	print("Решение не найдено!")