import numpy as np

a=np.random.randint(1,100,15)
print("Before sorting " , a)
a=np.sort(a)
print("after sorting ",a)

#sorting in descending
print("descending sort of a ", np.sort(a)[::-1])

b=np.random.randint(1,100,12).reshape(4,3)
print("Before sorting the 2d array \n",b)
print("After sorting the 2d array \n",np.sort(b)) #bydefault row wise
print("sorting b column wise of 2d array \n ", np.sort(b,axis=0)) #and if we put axis=1 it will sort row wise


#np.append

c=np.array([1,2,3])
c=np.append(c,200)
print(c)

a1=[1,2,3,4,5]
a1.append(90)
print(a1)