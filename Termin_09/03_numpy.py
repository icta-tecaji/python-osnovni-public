import numpy as np


# a = np.array([[1,2,3], [4,5,6]], dtype="float")
# print(a)
# #print(type(a))
# print(a.ndim)
# print(a.shape)
# print(a.size)
# print(a.dtype)

#a = np.zeros((3,3))
#a = np.ones((2, 10))
#a = np.empty((3, 4))
# a = np.full((2, 3), 44)
# print(a)
# print(type(a))

# a = np.arange(10, 45, 5)
# print(a)

# a = np.linspace(5, 10, 5)
# print(a)

# a = np.array([[1,2,3], [4,5,6]])
# b = a * 2
# print(a)
# print()
# print(b)

# b = a + a
# print(a)
# print()
# print(b)


# a = np.array([[1,2,3], 
#               [4,5,6]])
# print(a.sum())
# print(a.min())
# print(a.max())
# print(a.sum(axis=0))
# print(a.max(axis=1))

# a = np.array([0,1,2,3,4])
# print(a[2])
# print(a[1:-2])

# a = np.array([[0,1,2,3,4],
#               [5,6,7,8,9],
#               [10,11,12,13,14],
#               [15,16,17,18,19]])
# print(a[1,3])
# print(a[(1,3), 1:3])

# a = np.ones((2,3))
# print(a)
# print(a.shape)
# [1,1,1]
# [1,1,1]

# b = np.zeros(3)
# print(b)
# print(b.shape)
# b = b.reshape((1,3))

# c = np.concatenate((a,b), axis=0)
# print(c)

# a = np.random.randint(0,10, size=(6,4))
# print(a)
# filter_ = a < 6
# print(filter_)

# a[filter_] = 0
# print(a)