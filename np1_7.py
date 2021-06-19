import numpy as np
#------MIN MAX SUM------
a=np.array([[3,2,10,11],[5,2,12,13],[6,7,14,15],[8,9,16,17]])
#---min for minimum in a matrix------
print(a.min())
#---axis=0 is for all coloumn one by one in a matrix
print("min in coloumn",a.min(axis=0))
#---axis=1 is for all row one by one in a matrix
print("min in a row",a.min(axis=1))

#---max for maximum in a matrix------
print(a.max())
#---axis=0 is for all coloumn one by one in a matrix
print("max in coloumn",a.max(axis=0))
#---axis=1 is for all row one by one in a matrix
print("max in a row",a.max(axis=1))

print(np.sort(a,axis=0)
