'''
Use enumerate().
On each run, a line of the form "room x: y" should be printed,
where x is the index of the list element and y is the actual list element, i.e. the area.
Make sure to print out this exact string, with the correct spacing.
'''

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate()
for i, a in enumerate(areas) :
    print("room " + str(i) + ": " + str(a))
