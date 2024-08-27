import numpy as np
from matplotlib import pyplot as pt
def circularconvolution(x1,x2):
	z=[]
	for n in range(len(x1)):
		x2r=np.roll(x2,n)
		z.append(np.dot(x1,x2r))
	return z
x1=[1,2,3,4,5]
x2=[5,4,3,2,1]
y=circularconvolution(x1,x2)
pt.subplot(3,1,1)
pt.stem(x1)
pt.subplot(3,1,2)
pt.stem(x2)
pt.subplot(3,1,3)
pt.stem(y)
pt.show()
