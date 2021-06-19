import numpy as np
a=np.ones((8,8),dtype=int)
a[::2,::2]=0
a[1::2,1::2]=0
print(a)
