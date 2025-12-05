import numpy as np
import time

SIZE = 1000

lst1 = range(SIZE)
lst2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# Python list
start = time.time()
result = [(x+y) for x,y in zip(lst1, lst2)]
print("Python list took: ", (time.time()-start)*1000)

# Numpy array
start = time.time()
result = a1 + a2
print("Numpy took: ", (time.time()-start)*1000)

a = np.array([2, 'howru', 3.5])
print(a.shape)
