import numpy as np 
from matplotlib import pyplot as plt
signal=[1,2,3,4,5]
kernel=[0.2,0.5,0.2]
convolved_length=len(signal)+len(kernel)-1
convolved_signal=np.zeros(convolved_length)
for i in range(convolved_length):
	for j in range(len(kernel)):
		if i-j>=0 and i-j<len(signal):
			convolved_signal[i]+=signal[i-j]*kernel[j]
print(convolved_signal)
plt.subplot(3,1,1)
plt.stem(signal)
plt.subplot(3,1,2)
plt.stem(kernel)
plt.subplot(3,1,3)
plt.stem(convolved_signal)
plt.show()
convolution
import numpy as np
from matplotlib import pyplot as plt

x=[1,2,3,4,5]
y=[]
n=int(input("Enter the order of the signal"))
l=len(x)
p=l-n
for i in range(0,l):
	d=0
	if(i<n-1):
		a=0
		for j in range(0,i+1):
			a+=x[j]
		y.append(a/n)
	else:
		a=0
		for j in range(i+1-n,i+1):
			
			a+=x[j]
			
		y.append(a/n)
print(y)
plt.subplot(2,1,1)
plt.stem(x)
plt.subplot(2,1,2)
plt.stem(y)
plt.show()

