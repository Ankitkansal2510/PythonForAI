import numpy as np

a1=np.arange(10)
a2=np.arange(12,dtype=float).reshape(3,4) #1 block of size 3*4
a3=np.arange(8).reshape(2,2,2) #2 block of size 2*2(3d array

print(a1)
print(a2)
print(a3)

#Printing the dimension of the array

print("Printing the dimension of a1 array \n" , a1.ndim)
print("Printing the dimension of a2 array \n" , a2.ndim)
print("Printing the dimension of a3 array \n" , a3.ndim)

#Itemsize -it will tell how many memory consumption has been taken by array
print("printing the itemsize of a1 array \n" , a1.itemsize)
print("printing the itemsize of a2 array \n" , a2.itemsize)
print("printing the itemsize of a3 array \n" , a3.itemsize)


##changing the datatype of existing array
print("Checking the existing datatype of a1 array \n" , a1.dtype)
b=a1.astype(np.int32)
print("Checking the existing datatype of a1 array after chaning the datatype \n" , b.dtype)