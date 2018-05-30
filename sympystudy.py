import numpy as np
from pylab import *
from  sympy import *
import sys

def fun123(a,b):
	
	temp=solve(a,b)
	return temp

y='x**2-2'
x=Symbol('x')	
z=fun123(y,x)
print(z)

tmp = series(exp(I*x), x, 0, 10)
pprint(tmp)
