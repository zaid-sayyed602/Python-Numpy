import numpy as np
#----RESHAPING----
a=np.array([[2,3],[4,5],[6,7],[8,9]])
print(a.reshape(4,2))
b=np.array([[1,2,3,4,5,6,7,8,9,10,11,12]])
print(b.reshape(3,4))
#----b.reshape(no of rows,multiple coloumns)
print(b.reshape(1,-1))
#-----b.flatten() used to covert the matrix from 2D to 1D-------
print(b.flatten())

