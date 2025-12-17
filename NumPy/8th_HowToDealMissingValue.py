'''

how to deal with missing values

'''
import numpy as np

a=np.array([1,2,3,4,np.nan,5,6])
print("Actual array " , a)

a=a[~np.isnan(a)]
print("after removing missing value ", a)