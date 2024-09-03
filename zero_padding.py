import numpy as np
import matplotlib.pyplot as plt
def dft(x):
	X=[]
	for k in np.arange(0,len(x)):
		s=0
		for n in np.arange(0,len(x)): 
			s=s+x[n]*np.exp(-2j*np.pi*k*n/len(x))
		X.append(s)
	return X
m=[1,2,3,4,5,6,7,8,9]
k=np.arange(0,2*np.pi,(2*np.pi/len(m)))
q=dft(m)
l=[1,2,3,4,5,6,7,8,9,0,0,0,0,0]
e=np.arange(0,2*np.pi,(2*np.pi/len(l)))
w=dft(l)
plt.subplot(2,1,1)
plt.stem(k,np.abs(q))
plt.subplot(2,1,2)
plt.stem(e,np.abs(w))

plt.show()
