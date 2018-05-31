# Familiar functions
Out of the box, Python offers a bunch of built-in functions to make your life as a data scientist easier. You already know two such functions: print() and type(). You've also used the functions str(), int(), bool() and float() to switch between data types. These are built-in functions as well.
Calling a function is easy. To get the type of 3.0 and store the output as a new variable, result, you can use the following:
result = type(3.0)
The general recipe for calling functions and saving the result to a variable is thus:
output = function_name(input)

Requirement(s)
Use print() in combination with type() to print out the type of var1.
Use len() to get the length of the list var1. Wrap it in a print() call to directly print it out.
Use int() to convert var2 to an integer. Store the output as out2.
```
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
```

# Multiple arguments
In the previous exercise, the square brackets around imag in the documentation showed us that the argument is optional. But Python also uses a different way to tell users about arguments being optional.
Have a look at the documentation of sorted().
You'll see that sorted() takes three arguments: iterable, key and reverse.
key=None means that if you don't specify the key argument, it will be None. reverse=False means that if you don't specify the reverse argument, it will be False.
In this exercise, you'll only have to specify iterable and reverse, not key. The first input you pass to sorted() will be matched to the iterable argument, but what about the second input? To tell Python you want to specify reverse without changing anything about key, you can use =:
sorted(___, reverse = ___)
Two lists have been created for you on the right. Can you paste them together and sort them in descending order?
Note: For now, we can understand an iterable as being any collection of objects, e.g. a List.

Requirement(s)
Use + to merge the contents of first and second into a new list: full.
Call sorted() on full and specify the reverse argument to be True. Save the sorted list as full_sorted.
Finish off by printing out full_sorted.
```
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)

# Print out full_sorted
print(full_sorted)
```

# String Methods
Strings come with a bunch of methods. Follow the instructions closely to discover some of them. If you want to discover them in more detail, you can always type help(str) in the IPython Shell.
A string room has already been created for you to experiment with.

Requirement(s)
Use the upper() method on room and store the result in room_up. Use the syntax for calling methods that you learned in the previous video.
Print out room and room_up. Did both change?
Print out the number of o's on the variable room by calling count() on room and passing the letter "o" as an input to the method. We're talking about the variable room, not the word "room"!
```
# string to experiment with: room
room = "poolhouse"

# Use upper() on room: room_up
room_up = room.upper()

# Print out room and room_up
print(room)
print(room_up)

# Print out the number of o's in room
print(room.count("o"))
```

# List Methods
Strings are not the only Python types that have methods associated with them. Lists, floats, integers and booleans are also types that come packaged with a bunch of useful methods. In this exercise, you'll be experimenting with:
index(), to get the index of the first element of a list that matches its input and
count(), to get the number of times an element appears in a list.
You'll be working on the list with the area of different parts of a house: areas.

Requirement(s)
Use the index() method to get the index of the element in areas that is equal to 20.0. Print out this index.
Call count() on areas to find out how many times 14.5 appears in the list. Again, simply print out this number.
```
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 14.5 appears in areas
print(areas.count(14.5))
```

# List Methods (2)
Most list methods will change the list they're called on. Examples are:
append(), that adds an element to the list it is called on,
remove(), that removes the first element of a list that matches the input, and
reverse(), that reverses the order of the elements in the list it is called on.

Requirement(s)
Use append() twice to add the size of the poolhouse and the garage again: 24.5 and 15.45, respectively. Make sure to add them in this order.
Print out areas
Use the reverse() method to reverse the order of the elements in areas.
Print out areas once more.
```
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
```

# Import package
As a data scientist, some notions of geometry never hurt. Let's refresh some of the basics.
For a fancy clustering algorithm, you want to find the circumference, $C$, and area, $A$, of a circle. When the radius of the circle is r, you can calculate $C$ and $A$ as:
$$C = 2 \pi r$$ $$A = \pi r^2 $$
To use the constant pi, you'll need the math package.

Requirement(s)
Import the math package. Now you can access the constant pi with math.pi.
Calculate the circumference of the circle and store it in C.
Calculate the area of the circle and store it in A.
```
# Definition of radius
r = 0.43

# Import the math package
import math

# Calculate C
C = 2 * r * math.pi

# Calculate A
A = math.pi * r ** 2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))
```

# Selective import
General imports, like import math, make all functionality from the math package available to you. However, if you decide to only use a specific part of a package, you can always make your import more selective:
from math import pi
Let's say the Moon's orbit around planet Earth is a perfect circle, with a radius r (in km) that is defined in the script.

Requirement(s)
Perform a selective import from the math package where you only import the radians function.
Calculate the distance travelled by the Moon over 12 degrees of its orbit. Assign the result to dist. You can calculate this as r * phi, where r is the radius and phi is the angle in radians. To convert an angle in degrees to an angle in radians, use the radians() function, which you just imported.
Print out dist.
```
# Definition of radius
r = 192500

# Import radians function of math package
from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)

# Print out dist
print(dist)
```
