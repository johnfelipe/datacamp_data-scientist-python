'''
Adapt the print() function so that the first printout becomes
"room 1: 11.25", the second one "room 2: 18.0" and so on.
'''

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))
