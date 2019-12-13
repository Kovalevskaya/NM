# Решение системы линейных уравнений с трехдиагональной матрицей
import numpy as np

A=np.array([[435,4,0,0],[8,564,7,0],[0,5,395,33],[0,0,6,345]])
b=np.array([24,35,63,96])


def sol(A,b):
	d=np.array([A[i,i] for i in range(len(A))],float)
	l=np.array([A[i,i+1] for i in range(len(A)-1)],float)
	c=np.array([A[i+1,i] for i in range(len(A)-1)],float)
	r1=np.zeros(len(A),float)
	r1[1]=-l[0]/d[0]
	for i in range(2,len(A)):
		r1[i]=-l[i-1]/(d[i-1]+c[i-1]*r1[i-1])
	r2=np.zeros(len(A),float)
	r2[1]=b[0]/d[0]
	for i in range(2,len(A)):
		r2[i]=(-c[i-1]*r2[i-1]+b[i-1])/(d[i-1]+c[i-1]*r1[i-1])
	x=np.zeros(len(A),float)
	x[-1]=(-c[-1]*r2[-1]+b[-1])/(d[-1]+c[-1]*r1[-1])
	for i in range(len(A)-2,-1,-1):
		x[i]=r1[i+1]*x[i+1]+r2[i+1]
	return x
    
x = sol(A,b)
print(np.dot(A,x))