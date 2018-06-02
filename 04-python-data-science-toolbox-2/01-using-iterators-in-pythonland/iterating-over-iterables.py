'''
Create a for loop to loop over flash and print the values in the list. Use person as the loop variable. Create an iterator for the list flash and assign the result to superspeed. Print each of the items from superspeed using next() 4 times.
'''

# Create a list of strings: flash
flash = ['jay garrick', 'barry allen', 'wally west', 'bart allen']

# Print each list item in flash using a for loop
for person in flash:
    print(person)

# Create an iterator for flash: superspeed
superspeed = iter(flash)

# Print each item from the iterator
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))
print(next(superspeed))
