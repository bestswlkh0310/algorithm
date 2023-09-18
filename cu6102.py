import numpy as np

a = np.arange(10, 50)

print(a)

print(a[::-1])

b = np.arange(0, 9).reshape((3, 3))

print(b)

c = np.array([1,2,0,0,4])
print(c.nonzero())

print(np.eye(3, dtype=float))