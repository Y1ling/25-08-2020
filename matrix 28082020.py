# create a 4x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]

# use zip function to transpose the 4x3 matrix into a 3x4
x = list(zip(*matrix))
for i in range(len(x)):
    print(x[i])

# displaying two sequences in loop
Q = ['name', 'DOB', 'gender']
A = ['Yiling', '98/08/06', 'male']
for q, a in zip(Q, A):
    print('Your {0}? {1}'.format(q, a))


# use sorted function to return a new sorted sequence without changing the old one
basket = ['apple', 'orange', 'apple', 'peach', 'grape']
for f in sorted(set(basket)):
    print (f)


