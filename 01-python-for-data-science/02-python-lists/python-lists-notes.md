# Create a list 
As opposed to int, bool etc., a list is a compound data type; you can group values together:
a = "is"
b = "nice"
my_list = ["my", "list", a, b]
After measuring the height of your family, you decide to collect some information on the house you're living in. 
The areas of the different parts of your house are stored in separate variables for now, as shown in the script.

Requirement(s)
Create a list, areas, that contains the area of the hallway (hall), kitchen (kit), living room (liv), bedroom (bed) and bathroom (bath), in this order. Use the predefined variables.
Print areas with the print() function.
```
# Area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)
```

# Create list with different types
A list can contain any Python type. Although it's not really common, a list can also contain a mix of Python types including strings, floats, booleans, etc.

The printout of the previous exercise wasn't really satisfying. It's just a list of numbers representing the areas, but you can't tell which area corresponds to which part of your house.

Requirement(s)
Finish the line of code that creates the areas list such that the list first contains the name of each room as a string and then its area. More specifically, add the strings "hallway", "kitchen" and "bedroom" at the appropriate locations.
Print areas again.
```
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)
```

# List of lists
As a data scientist, you'll often be dealing with a lot of data, and it will make sense to group some of this data.

Instead of creating a flat list containing strings and floats, representing the names and areas of the rooms in your house, you can create a list of lists. 

Don't get confused here: "hallway" is a string, while hall is a variable that represents the float 11.25 you specified earlier.

Requirement(s)
Print out house.
Print out the type of house. 
```
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))
```

# Subset and conquer
Subsetting Python lists is easy. Take the code sample below, which creates a list x and then selects "b" from it. Remember that this is the second element, so it has index 1. You can also use negative indexing.
x = ["a", "b", "c", "d"]
x[1]
x[-3] # same result!

Requirement(s)
Print out the second element from the areas list, so 11.25.
Subset and print out the last element of areas, being 9.50. Using a negative index makes sense here!
Select the number representing the area of the living room and print it out.
```
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])
```

# Subset and calculate
After you've extracted values from a list, you can use them to perform additional calculations. Take this example, where the second and fourth element of a list x are extracted. The strings that result are pasted together using the + operator:
x = ["a", "b", "c", "d"]
print(x[1] + x[3])

Requirement(s)
Using a combination of list subsetting and variable assignment, create a new variable, eat_sleep_area, that contains the sum of the area of the kitchen and the area of the bedroom.
Print the new variable eat_sleep_area.
```
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = areas[3] + areas[-3]

# Print the variable eat_sleep_area
print(eat_sleep_area)
```

# Slicing and dicing
It's also possible to slice your list, which means selecting multiple elements from your list. 
Use the following syntax:
my_list[start:end]
The start index will be included, while the end index is not.
The code sample below shows an example. A list with "b" and "c", corresponding to indexes 1 and 2, are selected from a list x:
x = ["a", "b", "c", "d"]
x[1:3]
The elements with index 1 and 2 are included, while the element with index 3 is not.

Requirement(s)
Use slicing to create a list, downstairs, that contains the first 6 elements of areas.
Do a similar thing to create a new variable, upstairs, that contains the last 4 elements of areas.
Print both downstairs and upstairs using print().
```
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:10]

# Print out downstairs and upstairs
print(downstairs)
print(upstairs)
```

# Slicing and dicing (2)
In the video, Filip first discussed the syntax where you specify both where to begin and end the slice of your list:
my_list[begin:end]
However, it's also possible not to specify these indexes. If you don't specify the begin index, Python figures out that you want to start your slice at the beginning of your list. If you don't specify the end index, the slice will go all the way to the last element of your list. To experiment with this, try the following commands in the IPython Shell:
x = ["a", "b", "c", "d"]
x[:2]
x[2:]
x[:]

Requirement(s)
Use slicing to create the lists downstairs and upstairs again, but this time without using indexes if it's not necessary. Remember downstairs is the first 6 elements of areas and upstairs is the last 4 elements of areas.
```
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[6:]
```

# Replace list elements
Simply subset the list and assign new values to the subset to replace elements in a list. You can select single elements or you can change entire list slices at once.
x = ["a", "b", "c", "d"]
x[1] = "r"
x[2:] = ["s", "t"]

Requirement(s)
You did a miscalculation when determining the area of the bathroom; it's 10.50 square meters instead of 9.50.
Make the areas list more trendy! Change "living room" to "chill zone".

```
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Correct the bathroom area
areas[-1] = 10.50

# Change "living room" to "chill zone"
areas[4] = "chill zone"
```

# Extend a list
If you can change elements in a list, you sure want to be able to add elements to it. You can use the + operator:
x = ["a", "b", "c", "d"]
y = x + ["e", "f"]

Requirement(s)
Use the + operator to paste the list ["poolhouse", 24.5] to the end of the areas list. Store the resulting list as areas_1.
Further extend areas_1 by adding data on your garage. Add the string "garage" and float 15.45. Name the resulting list areas_2.
```
# Create the areas list (updated version)
areas = ["hallway", 11.25, "kitchen", 18.0, "chill zone", 20.0,
         "bedroom", 10.75, "bathroom", 10.50]

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage", 15.45]
```

# Inner workings of lists

The Python code in the script already creates a list with the name areas and a copy named areas_copy. Next, the first element in the areas_copy list is changed and the areas list is printed out. If you hit Run Code you'll see that, although you've changed areas_copy, the change also takes effect in the areas list. That's because areas and areas_copy point to the same list.
If you want to prevent changes in areas_copy to also take effect in areas, you'll have to do a more explicit copy of the areas list. You can do this with list() or by using [:].

Requirement(s)
Change the second command, that creates the variable areas_copy, such that areas_copy is an explicit copy of areas
Now, changes made to areas_copy shouldn't affect areas. 
```
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
```
