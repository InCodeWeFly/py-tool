import numpy as geek

# array = geek.arrange(8)
# The 'numpy' module has no attribute 'arrange'
array1 = geek.arange(8)
print("Original array : \n", array1)

# shape array with 2 rows and 4 columns
array2 = geek.arange(8).reshape(2, 4)
print("\narray reshaped with 2 rows and 4 columns : \n",
	array2)

# shape array with 4 rows and 2 columns
array3 = geek.arange(8).reshape(4, 2)
print("\narray reshaped with 2 rows and 4 columns : \n",
	array3)

# Constructs 3D array
array4 = geek.arange(8).reshape(2, 2, 2)
print("\nOriginal array reshaped to 3D : \n",
	array4)


# [
#  [ [0 1] [2 3] ]
#
#  [ [4 5] [6 7] ]
# ]








# https://numpy.org/doc/stable/reference/generated/numpy.reshape.html
