import numpy as np
import matplotlib.pyplot as mp
import cmath as cm
x=[6,4,5,3,2,3]
N=1000
j=cm.sqrt(-1)
X=[]
w=np.linspace(-np.pi,np.pi,N)
for i in range(0,N):
	sum=0
	for n in range(0,len(x)):
		sum=sum+(x[n]*np.exp(-j*w[i]*n))
	X.append(sum)
mp.subplot(221)
mp.plot(w,np.abs(X))
mp.xlabel("frequency")
mp.ylabel("magnitude")
mp.title("magnitude spectrum")
mp.grid()
mp.subplot(222)
mp.plot(w,np.angle(X))
mp.xlabel("frequency")
mp.ylabel("phase")
mp.title("phase spectrum")
mp.grid()
mp.show()

