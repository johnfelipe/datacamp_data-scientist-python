'''
Use pd.read_csv() to read in 'ind_pop.csv' in chunks of size 10. Assign the result to df_reader. Print the first two chunks from df_reader.
'''

# Import the pandas package
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv('ind_pop.csv', chunksize=10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))
