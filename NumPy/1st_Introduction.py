'''

The difference between nnumPy list and python list is :
Python list can stored mixed data type , each element is a python object

Numpy list stored only one data type (All ints , all floats etc)
Much more compact in memory
enable fast vatorised operation


Stores reference to Python object
High memory overhead per item

In numpy stored raw data to memory
less memory


In python list cannot perform mathematical operation directory

In mupy list , direct mathematical operation can be applied

'''

import numpy as np

print("1D array in numpy")
'''
since this is the 1-d array and 1-d array doesnt have row and column , it has one axis which has 3 columns
'''
a=np.array([1,2,3])
print(a)


print("2d array in numpy where shape will be 2 rows and 6 columns")
b=np.array([[1,2,3,4,5,6],
           [7,8,9,10,11,12]])
print(b)

print("2d array in numpy where shape will be 3 rows and 3 columns")
c=np.array([[3,4,5],
            [6,7,8],
            [9,10,11]
])

print(c)
print("3d array in numpy where shape will be 3 rows and 3 columns")
'''
For a 3D array, the shape looks like:

(dim1, dim2, dim3)


These represent:

Axis	Meaning	Example Description
Axis 0	Number of "blocks" / depth	How many 2D matrices
Axis 1	Number of rows in each block	Height
Axis 2	Number of columns in each row	Width
'''
l=np.array([
            [[1,2,3],
             [3,4,5],
             [6,7,8],
             [9,10,11]]])

print(l)
'''
here the number of block is 1 and 4 is the number of row and 3 is the number of column
'''
print("The shape of 3d array l is " , l.shape)

print("Another example of 3d array where we will increase the block ")
m=np.array([
    [[1,2,3],
     [3,4,5]],

    [[6,7,8],
     [9,10,11]]
])
'''
a = np.array([
    [[1, 2, 3],
     [4, 5, 6]],

    [[7, 8, 9],
     [10, 11, 12]]
])

Block 0:
[ [1, 2, 3],
  [4, 5, 6] ]

Block 1:
[ [7, 8, 9],
  [10, 11, 12] ]'''
print("Printing 3d array m of block 2 rows where each block is 2*3 matrix ",m)
print("Printing the 3d array shape of m where we have increase the block", m.shape)
print("Can directly apply mathematical operation on numpy list")
d=np.array([1,2,3,4,5,6])*2
print(d)

print("Type of numpy array a is ")
print(type(a))

print("size of numpy array a is ")
print(a.size)

print("Shape of numpy array a is ")
## only one row and 3 column so output will be 3,
print(a.shape)


print("Shape of numpy array b is ")
print(b.shape)

##Shape will give the number of rows and columns
print("Shape of numpy array c is ")
print(c.shape)

print("data type of numpy array a is ")
print(a.dtype)

'''
Transpose will replace rows with columns 
'''
print("Transpose of the array b is ", b.transpose())

## arange() function  this will create the array for the given range

arange=np.arange(1,11)
print("arange of array")
print(arange)


##reshape , it will reshape the array 5 rows and 2 columns
re_shape=np.arange(1,11).reshape(5,2)
print("Reshaped array is ")
print(re_shape)


##np.ones , it will create array where all element are 1,
#similary there is np.zeros and np.random

ones=np.ones((2,3)) ##It will create 2*3 matrix of element 1
print("np ones example " , ones)


##np.linespace
# we will provide 3 parameters , lower range , upper range and number of items we want to generate
#It will generate equal distance numbers
linespace=np.linspace(-10,10,10)
print("np linespace example \n" , linespace)

##Np.identity It will create identity matrix , where diognal element are 1 and all others are 0

identity=np.identity(3)
print("np identity example \n" , identity)