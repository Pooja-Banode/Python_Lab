import numpy as np

# Creating a 1D array of values from 2 to 10 (inclusive)
values = np.arange(2, 11)  # np.arange(start, stop), stop is exclusive, so we use 11

# Reshaping the 1D array into a 3x3 matrix
matrix = values.reshape(3, 3)

print("3x3 Matrix with values ranging from 2 to 10:")
print(matrix)




#output

'''3x3 Matrix with values ranging from 2 to 10:
[[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]
'''
