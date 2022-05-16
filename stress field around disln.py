import matplotlib.pyplot as plt
import numpy as np
from pylab import cm

l=20
n=551
d=1

x=np.linspace(-l,l,n)
y=np.linspace(-l,l,n)

X,Y=np.meshgrid(x,y)

sigxy= d*X*(X**2-Y**2)/(X**2+Y**2)**2

sig_max=0.1
sig_min=0.1

plt.pcolor(X,Y,sigxy,cmap=cm.RdBu,vmin= sig_min,vmax=sig_max)
plt.colorbar()
plt.title("shear stress around dislocation")