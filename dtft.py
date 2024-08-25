import numpy as np
import matplotlib.pyplot as plt
X=[]
n=np.arange(0,500)
x=np.sin(2*np.pi*(200/8000)*n) 
N=len(x)
omega=np.arange(-1*np.pi,np.pi,0.001*np.pi)
for i in range(0,len(x)):
    X.append(x[i]*np.exp(-1j*omega*i))
s=sum(X)
s1=np.abs(s)
s2=np.angle(s)
m=np.argmax(s1)
print("peak value at: ",omega[m])
plt.plot(omega,s1)
plt.plot(omega,s2)
plt.show()
