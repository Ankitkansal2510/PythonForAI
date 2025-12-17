'''

There are many built in funciton in numpy for example np.sum() np.sign() etc

but if we want to create our own function then how do we do that


Lets create signmoid function formula is

σ(x)=1/1+e−x1

now how we will create this in python
'''
import numpy as np


def sigmoid(array):
    return 1/(1+np.exp(-array))

a=np.arange(10)
print(sigmoid(a))
