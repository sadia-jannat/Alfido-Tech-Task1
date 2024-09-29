import numpy as np
import matplotlib.pyplot as plt
# if using a Jupyter notebook, inlcude:
#matplotlib inline

x = np.arange(0,4*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)

fig, ax = plt.subplots()

ax.plot(x,y)
ax.plot(x,z)

plt.show()