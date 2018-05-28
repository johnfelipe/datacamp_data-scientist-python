'''
Inside the while loop, replace offset = offset - 1 by an if-else statement:
If offset > 0, you should decrease offset by 1.
Else, you should increase offset by 1.
'''

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
        offset = offset - 1
    else :
        offset = offset + 1
    print(offset)
