# Exercise_03
```python
import numpy as np
from matplotlib import pyplot as plt
t0=0
v0=0
tf=10
n=10
deltax=(tf-t0)/(n-1)
t=np.linspace(t0,tf,n)
v=np.zeros([n]);
v[0]=v0;
for i in range(1,n):
    v[i]=deltax*(-9.8)+v[i-1]
    for i in range(n):
        print(t[i],v[i])
        
plt.plot(t,v,'0')
plt.xlabel("t-axis")
plt.ylabel("v-axis")
plt.show()
