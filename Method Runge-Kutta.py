﻿#Метод Рунге-Кутта 4-го порядка
import numpy as np
from math import sin, pi
import matplotlib.pyplot as plt

def Sol(F, tau, T, y0):
	N = int(T/tau)+1
	t = np.array([tau*n for n in range(0, N)])
	y = np.zeros((N, len(y0)), float)
	y[0] = y0
	k = 0
	print(y)
	while tau*(k+1) < T:
		k1 = F(tau[k], y[k])
		k11 = [tau*i/2 for i in k1]
		k2 = F(t[k] + tau/2, y[k] + k11)
		k22 = [tau*i/2 for i in k2]
		k3 = F(t[k] + tau/2, y[k] + k22)
		k33 = [tau*i for i in k3]
		k4 = F(t[k] + tau, y[k] + k33)
		k2 = np.array([2*i for i in k2])
		k3 = np.array([2*i for i in k3])
		temp = np.array(k1 + k2 + k3 + k4)
		K = np.array([tau/6*i for i in temp])
		y[k+1] = y[k] + K
		k += 1
	print(y)
	return t, y

def F(tn, yn):
	return np.array([yn[1], -sin(yn[0])])

t, y = Sol(F, pi/50, 4*pi, [1, 0])
u = np.array(y[:,0])
print(u)
plt.plot(t, u, label="RK")
plt.legend()
plt.ylabel("y[t]")
plt.xlabel("x")
plt.show()
