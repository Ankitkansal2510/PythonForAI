import numpy as np

a=np.arange(12).reshape(4,3)
print(a)

'''
if we have some pattern for example we need alternate rows or something where we can form pattern then we can 
use simple indecxing that way we did earlier for example 
if we want  4,5,7,8,

then we will do something

a[1:3,1:3] meaning row 1 se 2 and column 1 se 2 we used 3 because that last part is exclusive 

Now if we want to print 0th row 2nd row and 3rd row -> In this it is difficulat 
as there is no pattern using which we can create our formula so we will use fancy indexing

Fancy indexing
in Fancy indexing, we will pass the number of rows which we need as a list 

a[[0,2,3]]
'''

print("Example of fancy indexing for rows \n" ,  (a[[0,2,3]]))

#now we want 1st column and second column
print("Example of fancy indexing for columns \n" ,a[:,[1,2]] )

##Bolean indexing
'''it is used where we need some condition to pick element 
for example , number greator than 50 
number <0
like this 

'''

a1=np.random.randint(1,100,24).reshape(6,4)
#RandInt is a function , it accepts 3 argument , 1st argument is start number
#second argument is end number , 3rd argumnet is how many numbers
print("printing a1 array \n" ,a1)

#find all number> 50
print("printing elements greator than 50 from a1 array \n" , a1[a1>50])

#print element >50 and are even
print("printing elements greator than 50 from a1 array \n" , a1[(a1>50) & (a1%2==0)])