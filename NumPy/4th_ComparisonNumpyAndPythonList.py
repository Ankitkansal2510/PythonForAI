##Speed test between python list vs numply list
import time
import numpy as np
import sys
a=[i for i in range(10000000)]
b=[i for i in range(10000000,20000000)]
c=[]

print(d)
start=time.time()
for i in range(len(a)):
    c.append(a[i]+b[i])

print("print the time for python list ", time.time()-start)
#print("printing the result of c after adding python array , " , c)
print("Checking the size of a used ", sys.getsizeof(a))

a1=np.arange(10000000)
b1=np.arange(10000000,20000000)
start1=time.time()
d=a+b
print("print the time for the numpy list " , time.time()-start1)
print("Checking the size of a1 used ", sys.getsizeof(a1))
#print("printing the result of d after adding numpy array , " , d)

##This differece of time clearly shows numpy is very fast as compared to python list

##size is almost same but in numpy there is a flexibility to store lesser intdatatype for example
a2=np.arange(10000000,dtype=np.int8)
print("Checking the size of a2 used ", sys.getsizeof(a2))
