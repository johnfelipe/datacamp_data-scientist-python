'''
Create a DataFrame medium,
that includes all the observations of cars that have a cars_per_cap between 100 and 500.
Print out medium.
'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
between = np.logical_and(cars["cars_per_cap"] > 100,
    cars["cars_per_cap"]  < 500)
medium = cars[between]

# Print medium
print(medium)
