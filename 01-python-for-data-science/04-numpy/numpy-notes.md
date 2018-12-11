# Your First NumPy Array
In this chapter, we dive into the world of baseball. Along the way, you'll get comfortable with the basics of numpy, a powerful package to do data science.
A list baseball has already been defined in the Python script, representing the height of some baseball players in centimeters. 

Requirement(s) 
Import the numpy package as np, so that you can refer to numpy with np.
Use np.array() to create a numpy array from baseball. Name this array np_baseball.
Print out the type of np_baseball to check that you got it right.
```
# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))
```

# Baseball players' height
You are a huge baseball fan. You decide to call the MLB (Major League Baseball) and ask around for some more statistics on the height of the main players. They pass along data on more than a thousand players, which is stored as a regular Python list: height. The height is expressed in inches. 
(Source: stat.ucla.edu).

Requirement(s)
Create a numpy array from height. Name this new array np_height.
Print np_height.
Multiply np_height with 0.0254 to convert all height measurements from inches to meters. Store the new values in a new array, np_height_m.
Print out np_height_m and check if the output makes sense.
```
# height is available as a regular list

# Import numpy
import numpy as np

# Create a numpy array from height: np_height
np_height = np.array(height)

# Print out np_height
print(np_height)

# Convert np_height to m: np_height_m
np_height_m = np_height * 0.0254

# Print np_height_m
print(np_height_m)
```

# Baseball player's BMI
The MLB also offers to let you analyze their weight data. Again, both are available as regular Python lists: height and weight. height is in inches and weight is in pounds.
It's now possible to calculate the BMI of each baseball player. 

Requirement(s)
Create a numpy array from the weight list with the correct units. Multiply by 0.453592 to go from pounds to kilograms. Store the resulting numpy array as np_weight_kg.
Use np_height_m and np_weight_kg to calculate the BMI of each player.
Print out bmi.
```
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254

# Create array from weight with correct units: np_weight_kg
np_weight_kg = np.array(weight) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2

# Print out bmi
print(bmi)
```

# Lightweight baseball players
To subset both regular Python lists and numpy arrays, you can use square brackets:
x = [4 , 9 , 6, 3, 1]
x[1]
import numpy as np
y = np.array(x)
y[1]
For numpy specifically, you can also use boolean numpy arrays:
high = y > 5
y[high]

Requirement(s)
Create a boolean numpy array: the element of the array should be True if the corresponding baseball player's BMI is below 21. You can use the < operator for this. Name the array light.
Print the array light.
Print out a numpy array with the BMIs of all baseball players whose BMI is below 21. Use light inside square brackets to do a selection on the bmi array.
```
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height) * 0.0254
np_weight_kg = np.array(weight) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])
```

# Subsetting NumPy Arrays
Python lists and numpy arrays sometimes behave differently. Luckily, there are still certainties in this world. For example, subsetting (using the square bracket notation on lists or arrays) works exactly the same. 
x = ["a", "b", "c"]
x[1]
np_x = np.array(x)
np_x[1]

Requirement(s)
Subset np_weight: print out the element at index 50.
Print out a sub-array of np_height: It contains the elements at index 100 up to and including index 110
```
# height and weight are available as a regular lists

# Import numpy
import numpy as np

# Store weight and height lists as numpy arrays
np_weight = np.array(weight)
np_height = np.array(height)

# Print out the weight at index 50
print(np_weight[50])

# Print out sub-array of np_height: index 100 up to and including index 110
print(np_height[100:111])
```

# Your First 2D NumPy Array
Before working on the actual MLB data, let's try to create a 2D numpy array from a small list of lists.
In this exercise, baseball is a list of lists. The main list contains 4 elements. Each of these elements is a list containing the height and the weight of 4 baseball players, in this order. 

Requirement(s)
Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.
Print out the type of np_baseball.
Print out the shape attribute of np_baseball. Use np_baseball.shape.
```
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
```

# Baseball data in 2D form
You have another look at the MLB data and realize that it makes more sense to restructure all this information in a 2D numpy array. This array should have 1015 rows, corresponding to the 1015 baseball players you have information on, and 2 columns (for height and weight).
The MLB was, again, very helpful and passed you the data in a different structure, a Python list of lists. In this list of lists, each sublist represents the height and weight of a single baseball player. The name of this embedded list is baseball.

Requirement(s)
Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.
Print out the shape attribute of np_baseball.
```
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)
```

# Subsetting 2D NumPy Arrays
If your 2D numpy array has a regular structure, i.e. each row and column has a fixed number of values, complicated ways of subsetting become very easy. Have a look at the code below where the elements "a" and "c" are extracted from a list of lists.

#regular list of lists
x = [["a", "b"], ["c", "d"]]
[x[0][0], x[1][0]]
#numpy
import numpy as np
np_x = np.array(x)
np_x[:,0]

For regular Python lists, this is a real pain. For 2D numpy arrays, however, it's pretty intuitive! The indexes before the comma refer to the rows, while those after the comma refer to the columns. The : is for slicing; in this example, it tells Python to include all rows.

Requirement(s)
Print out the 50th row of np_baseball.
Make a new variable, np_weight, containing the entire second column of np_baseball.
Select the height (first column) of the 124th baseball player in np_baseball and print it out.
```
# baseball is available as a regular list of lists

# Import numpy package
import numpy as np

# Create np_baseball (2 cols)
np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight
np_weight = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123, 0])
```

# 2D Arithmetic
Remember how you calculated the Body Mass Index for all baseball players? numpy was able to perform all calculations element-wise (i.e. element by element). For 2D numpy arrays this isn't any different! You can combine matrices with single numbers, with vectors, and with other matrices.

import numpy as np
np_mat = np.array([[1, 2],
                   [3, 4],
                   [5, 6]])
np_mat * 2
np_mat + np.array([10, 10])
np_mat + np_mat

Requirement(s)
np_baseball is a 2D numpy array with 3 columns representing height, weight and age
You managed to get hold of the changes in weight, height and age of all baseball players. It is available as a 2D numpy array, updated. Add np_baseball and updated and print out the result.
You want to convert the units of height and weight. As a first step, create a numpy array with three values: 0.0254, 0.453592 and 1. Name this array conversion.
Multiply np_baseball with conversion and print out the result.
```
# baseball is available as a regular list of lists
# updated is available as 2D numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)
```

# Average versus median
You now know how to use numpy functions to get a better feeling for your data. It basically comes down to importing numpy and then calling several simple functions on the numpy arrays:
import numpy as np
x = [1, 4, 8, 10, 12]
np.mean(x)
np.median(x)
The baseball data is available as a 2D numpy array with 3 columns (height, weight, age) and 1015 rows. The name of this numpy array is np_baseball. After restructuring the data, however, you notice that some height values are abnormally high. Follow the instructions and discover which summary statistic is best suited if you're dealing with so-called outliers.

Requirement(s)
Create numpy array np_height that is equal to first column of np_baseball.
Print out the mean of np_height.
Print out the median of np_height.
```
# np_baseball is available

# Import numpy
import numpy as np

# Create np_height from np_baseball
np_height = np_baseball[:,0]

# Print out the mean of np_height
print(np.mean(np_height))

# Print out the median of np_height
print(np.median(np_height))
```

# Explore the baseball data
Because the mean and median are so far apart, you decide to complain to the MLB. They find the error and send the corrected data over to you. It's again available as a 2D Numpy array np_baseball, with three columns.

Requirement(s)
Complete the code for the median height.
Use np.std() on the first column of np_baseball to calculate stddev. Replace None with the correct code.
Do big players tend to be heavier? Use np.corrcoef() to store the correlation between the first and second column of np_baseball in corr. Replace None with the correct code.
```
# np_baseball is available

# Import numpy
import numpy as np

# Print mean height (first column)
avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))
```

# Blend it all together
Now it's time to dive into another sport: soccer.
You've contacted FIFA for some data and they handed you two lists. The lists are the following:
positions = ['GK', 'M', 'A', 'D', ...]
heights = [191, 184, 185, 180, ...]
Each element in the lists corresponds to a player. The first list, positions, contains strings representing each player's position. The possible positions are: 'GK' (goalkeeper), 'M' (midfield), 'A' (attack) and 'D' (defense). The second list, heights, contains integers representing the height of the player in cm. The first player in the lists is a goalkeeper and is pretty tall (191 cm).
You're fairly confident that the median height of goalkeepers is higher than that of other players on the soccer field. Some of your friends don't believe you, so you are determined to show them using the data you received from FIFA.

Requirement(s)
Convert heights and positions, which are regular lists, to numpy arrays. Call them np_heights and np_positions.
Extract all the heights of the goalkeepers. You can use a little trick here: use np_positions == 'GK' as an index for np_heights. Assign the result to gk_heights.
Extract all the heights of all the other players. This time use np_positions != 'GK' as an index for np_heights. Assign the result to other_heights.
Print out the median height of the goalkeepers using np.median().
Do the same for the other players. Print out their median height. 
```
# heights and positions are available as lists

# Import numpy
import numpy as np

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_positions = np.array(positions)
np_heights = np.array(heights)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Print out the median height of goalkeepers. Replace 'None'
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Print out the median height of other players. Replace 'None'
print("Median height of other players: " + str(np.median(other_heights)))
```
