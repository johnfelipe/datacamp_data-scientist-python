'''
In the inner list comprehension - that is, the output expression of the nested list comprehension - create a list of values from 0 to 4 using range(). Use col as the iterator variable. In the iterable part of your nested list comprehension, use range() to count 5 rows - that is, create a list of values from 0 to 4. Use row as the iterator variable; note that you won't be needing this to create values in the list of lists.
'''

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0,5)] for row in range(0,5)]

# Print the matrix
for row in matrix:
    print(row)
