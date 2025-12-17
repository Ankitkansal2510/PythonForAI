import numpy as np

a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(3,4)

print("a1 \n" , a1)
print("a2 \n" , a2)

#Scaler operation
#Multiplying every elemetns by 2
print("multiply operators \n " , a1*2)

#Relational operator

print("Relational operators \n " , a2>15)

#Vector operator adding two array
print("adding two if size are same \n",a1+a2)

print("Printing the maximum number from a1 \n ",np.max(a1))
print("Printing the sum of all  number from a1 \n ",np.sum(a1))
print("Printing the product of all elem from a1 \n ",np.prod(a1))

#If i want to find the minimum of each row
print("printing the minimum of each row from a1 array \n ",np.min(a1,axis=1)) # 0 mean col and 1 mean row


#mean/median/standard deveiation /variance

#Log and exponents

print("Printing the log of array a2 \n ", np.log(a2))

#Indexing and slicing

m1=np.arange(10)
m2=np.arange(12).reshape(3,4)
m3=np.arange(8).reshape(2,2,2)
print("Printing m1 \n " , m1)
print("First index of the array m1 \n" , m1[0]) #it will access first index from start
print("last index of the array m2 \n" , m1[-1]) #-1 mean it will access first index from the last

'''Since this is the 1-D array it is easy to access the element , but how to access element in case of 2-d ,3d ...nd array

'''

print("Printing m2 \n " , m2)
print("Printing m2 specific index \n " , m2[1,3])  #meaning locate the element in 1st row and 3rd column

#Now how to get for 3d array
print("printing 3d array m3 \n", m3)
print("print the specific element at some index for example 7 \n" , m3[1,1,1])
#there are two blocks at index 0 and 1 , so first argument is block ,
# second argument is row
# third argument is column

#Slicing : can take out multiple item , like in indexing only one item at specific index can be print , in slicing multiple can be picked


print("Slicing from m1 \n", m1[2:5]) #first index is inclusive and 2nd index is exclusive

print("slicing from m2 for 0th row and all column \n" , m2[0,:])
print("slicing from m2 for all row and 3rd column \n" , m2[:,2])
print("slicing element 5,6,9,10 \n" , m2[1:,1:3]) # it mean 1st row onwards , and themn 1st column to second column

print("slicing element 0,3,8,11 \n" , m2[::2,::3])
##meaning first colon mean all rows
# second colun with 2  i.e :2 mean alternate
#now for column part i.e ::3 , it mean all column and skiiping two column

print("slicing element 1,3,9,11 \n" , m2[::2,1::2])
print("slicing element 4 and 7 \n" , m2[1,::3])
print("slicing element 5,6, 7 \n" , m2[1,1:4])



#now lets learn slicing with 3d array

m4=np.arange(27).reshape(3,3,3)
print("Printing m4 array which is 3d \n " , m4)


print("print 1st block i.e. 9,10,11,12,13,14,15,16,17 \n ", m4[1,:,:])

#loops
#This way loop will print the complete block if it is 2d array then first iteration 1st block and go on not iterate the each element

for i in m1:
    print("Printing loop element in m1 " , i)

for i in m2:
    print("Printing loop element in m2 \n" , i)

for i in m3:
    print("Printing loop element in m3 \n" , i)

##if want to print each element
##using nditer it will first convert each to 1d array and then print each element
for i in np.nditer(m2):
    print("Printing loop element in m2 using iterator \n" , i)

#Example of hsplit i.e. horizontal split
n1=np.arange(12).reshape(3,4)
print("printing n1 2d array " , n1)
print("now we are splitting the n1 array to horizontal split \n" , np.hsplit(n1,2))
# we can only solit till number of columns , example in above array there are 4 columns so maximum it can
#be split till 4