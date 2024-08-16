import numpy as np

arr_1 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90], dtype = 'int8')
print(arr_1)

# Numpy Array In-Built Methods & Properties
print(arr_1.shape)      # shape returns (rows,columns)
print(type(arr_1))      
print(arr_1.dtype)      # dtype returns data-type
print(arr_1.itemsize)   
print(arr_1.size)       # size() - Returns Total size of Array
print(arr_1.ndim)       # Dimentionality - 1D
print(arr_1.nbytes)     # nbytes = Total size of Numpy Array

# Types of Numpy Array
# Create 1-D Array
arr_2 = np.array([10, 15, 17, 21, 23, 44, 65, 89])

# Create a 2-D Array - Matrix
arr_3 = np.array([[18, 11, 13, 15],
                  [33, 75, 10, 39],
                  [41, 54, 47, 25]])

# shape returns (rows , columns)
print(arr_3.shape)
print(arr_3.ndim)
print(arr_3.itemsize)

# Three dimension (3-D) array
arr_4 = np.array([[[18, 11, 13, 15, 45],
                   [33, 75, 10, 39, 22],
                   [41, 54, 47, 25, 89]],

                   [[12, 15, 76, 17, 23],
                   [33, 75, 199, 59, 79],
                   [41, 54, 13, 44, 9]]])

# shape returns (matrics, rows , columns)
print(arr_4.shape)
print(arr_4.ndim)
print(arr_4.itemsize)

# slicing & Indexing in Numoy Array
print(arr_3[0])         # Indexing for first row elements
print(arr_3[:,:])       # All rows & all columns
print(arr_3[:,0])       # Slicing elements from all rows & first column index
print(arr_3[:,0:2])     # Slicing first two columns 

print(arr_3[1:-1,1:-1])  # start index = 1, stop index = last index position.
# slicing 3-D numpy array
print(arr_4[1,1,2])

# Create Numpy Array using Functions
arr_5 = np.arange(1,51)    # Create 1-D Array
print(arr_5)

arr_6 = np.arange(1,51).reshape(10,5)
print(arr_6)

# zero matrix : np.zero(shape)
arr_7 = np.zeros((5,7), dtype = 'int16')
print(arr_7)
print(arr_7.astype('float16'))   # Type Casting from int to float

# ones matrix
arr_8 = np.ones((5,5))
print(arr_8)

# identity matrix
arr_9 = np.identity(7)   # identity will be square matrix.
print(arr_9)

# empty matrix
arr_10 = np.empty((6,1))
print(arr_10)

# fill all position with 2.0 float value.
arr_10.fill(2.0)
print(arr_10)

# full 
print(np.full(10, 6.1))

# linspace - (start,stop,elements) 
# linspace create N evenly spaced array , here N is num of elements
arr_11 = np.linspace(10, 100, 10)
print(arr_11)

# logspace - N evenly spaced array elements on a log scale between start and stop (log base 10.)
arr_12 = np.logspace(0, 1, 10, base=10)
print(arr_12)

# Exercise - 1
array_1 = np.ones((10,10))
array_1[1:-1,1:-1] = 0
# array_1[1:-1,1:-1].fill(0)
print(array_1)

# Exercise - 2
array_2 = np.ones((10,10))
array_2[::2,::2] = 0
array_2[1::2,1::2] = 0
print(array_2)

# Mathematical Operations - Numpy Array
arr_13 = np.array([[[1, 3, 5],
                   [4, 8, 7],
                   [9, 11, 13]],

                   [[2, 4, 7],
                   [3, 1, 5],
                   [5, 2, 8]]])
print(arr_13.sum())
# rowwise summation
print(arr_13.sum(axis = 0))
# columnwise summation
print(arr_13.sum(axis = 1))
# min()
arr_13.min()

# max()
arr_13.max()

# where() - returns index position for condition = True
arr_14 = np.arange(1,21).reshape(5,4)
print(np.where(arr_14 > 8))

# Statistical Methods
arr_15 = np.arange(1,37).reshape(6,6)
arr_15.mean()           # calculate mean()
arr_15.mean(axis = 0)   # calculate mean - Rowwise
arr_15.mean(axis = 1)   # calculate mean - Columnwise

np.std(arr_15)          # standard deviation
np.var(arr_15)          # variance

# Reversing an Array
array_3 = np.arange(50)
print(array_3)
# step size = -1
array_3[0::-1]

# flip the array 
print(np.flip(arr_6))
# flip the rows up & down
print(np.flipud(arr_6))
# flip the columns left & right
print(np.fliplr(arr_6))

# Flatten - To convert N-D Array into 1-D Array
array_4 = np.random.randint(10,99, size = (5,3))
print(array_4)

# 2D array to 1D Array
print(array_4.flatten())

# ravel() - Flattens N-D array to 1-D Array
print(array_4.ravel())

# np.argmax() - Returns Index Position of Maximum Value along axis.
array_5 = np.array([1, 2, 8, 11, 3, 6, 7, 13, 5, 7])
print(np.argmax(array_5))
print(np.argmax([0, 0, 0, 0.8, 0.05, 0.05, 0.1, 0, 0]))

print(array_4)
print(np.argmax(array_4))