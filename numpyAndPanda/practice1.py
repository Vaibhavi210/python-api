
import numpy as np 

ones=np.ones((5,5))
print(ones)
zeros=np.zeros((3,3))
print(zeros)
zeros[1,1]=9
print(zeros)
ones[1:4,1:4]=zeros
print(ones)