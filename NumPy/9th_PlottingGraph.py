''''
potting a graph
x=y

'''

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10,100) #from range -10 to 10 we took 100 numbers which are eual distance
y=x;

plt.plot(x,y)
plt.show()

#now show y=x power 2

y=x*x
plt.plot(x,y)
plt.show()

y=np.sin(x)
plt.plot(x,y)
plt.show()