'''
Write a generator expression that will generate the lengths of each string in lannister. Use person as the iterator variable. Assign the result to lengths. Supply the correct iterable in the for loop for printing the values in the generator object.
'''

# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(person) for person in lannister)

# Iterate over and print the values in lengths
for value in lengths:
    print(value)
