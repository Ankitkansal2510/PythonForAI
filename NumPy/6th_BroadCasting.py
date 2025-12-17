'''Broadcasting in NumPy

Broadcasting is a core NumPy mechanism that allows arithmetic operations between arrays of different shapes without explicitly copying data. NumPy virtually “stretches” the smaller array so that element-wise operations can be performed efficiently.

Why broadcasting exists

Avoids writing explicit loops (vectorization).

Saves memory (no real data duplication).

Makes numerical code concise and expressive.

Broadcasting rules (formal definition)

When operating on two arrays, NumPy compares their shapes from right to left (trailing dimensions):

For each dimension pair:

They are equal, or

One of them is 1

If neither condition is met, broadcasting fails with a ValueError.
'''
import numpy as np
a=np.arange(12).reshape(4,3)
b=np.arange(3)

print(a)
print(b)

'''
now we have two arrays one is size 3*4 and another is 1d array of size 3 
i.e (4,3) and (3,)

now as a rule we will first convert 1-d array to 2d array by adding 1 into head of 1d

i.e (4,3) and (1,3)

now in smaller array(1,3) increase the 1 to match the rows in the bigger array  now it will become 

(4,3) and (4,3)

it is possible 
'''

print("In tbis example broadcasting is possible hence able to add two array \n " , a+b)

#Another example where broadcasting is not possible and it will give error

a1=np.arange(12).reshape(3,4)
b1=np.arange(3)
print("Broadcasting not possible \n ", a1+b1)

'''now we have two arrays one is size 3*4 and another is 1d array of size 3 
i.e (3,4) and (3,)

now as a rule we will first convert 1-d array to 2d array by adding 1 into head of 1d

i.e (3,4) and (1,3)

now in smaller array(1,3) increase the 1 to match the rows in the bigger array  now it will become 

(3,4) and (3,3)

now both are still now equal , hence broadcasting is not possible and this will gice error

'''