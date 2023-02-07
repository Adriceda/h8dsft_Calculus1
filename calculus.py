import numpy as np
import matplotlib.pyplot as plt
import sympy as sy

x = sy.Symbol('x', real=True)

y1 = x**2 + 2*x + 1
y2 = 4*x**3 - 3*x**2 + 2*x - 1 

#USING SYMPY
y1dev = y1.diff(x)
y2dev = y2.diff(x)

print('y1 = ', y1)
print('y2 = ', y2)
print('using SYMPY y1dev = ', y1dev)
print('using SYMPY y2dev = ', y2dev)



#USING NUMPY

# z = np.linspace(0,20)
# a1 = z**2 + 2*z + 1
# a2 = 4*z**3 - 3*z**2 + 2*z - 1 


# df1 = np.diff(a1)/np.diff(z)
# df2 = np.diff(a2)/np.diff(z)

# df11 = np.gradient(a1, z)
# df22 = np.gradient(a2, z)

# print('numpy dev1', df1, df11)
# print('numpy dev2', df2, df22)