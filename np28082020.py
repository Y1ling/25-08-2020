from numpy import *
# create a random 1x4 matrix
a = random.rand(1,4)
print (a)

# create a row vector
vector1 = array([1, 2, 3])
print (vector1)

# create a column vector
vector2 = array([[1], [2], [4]])
print(vector2)

# create another row vector
vector3 = array([6, 4, 9])

# apply dot product rule on two vectors
print(dot(vector1, vector3))

# create 2 matrices for calculation
mat1 = array([[1, 2, 3], [4, 2, 8], [6, 4, 9]])
mat2 = random.rand(3, 3)
print(mat1)
print(mat2)

# add 2 matrices together
print(mat1 + mat2)

# apply dot rule on them
print(dot(mat1, mat2))

