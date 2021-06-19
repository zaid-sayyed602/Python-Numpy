import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[11,12,13],[14,15,16],[17,18,19]])
#-------ADDITION OF TWO MATRIX----------
c=a+b
print(c)
c=np.add(a,b)
print(c)
#-------MULT OF TWO MATRIX----------
c=a*b
c=np.matmul(a,b)
c=np.dot(a,b)
print(c)
