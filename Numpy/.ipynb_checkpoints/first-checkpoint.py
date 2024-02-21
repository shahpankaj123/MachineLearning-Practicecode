import numpy as np

a = np.arange(6)
a2 = a[np.newaxis, :]
a2.shape
print(a2)


a1 = np.array([1, 2, 3, 4, 5, 6])
print(a1)