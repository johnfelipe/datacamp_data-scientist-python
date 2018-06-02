'''
Use pd.read_csv() to read in the file 'ind_pop_data.csv' in chunks of size 1000. Assign the result to urb_pop_reader. Write a list comprehension to generate a list of values from pops_list for the new column 'Total Urban Population'. Use tup as the iterator variable. The output expression should be the product of the first and second element in each tuple in pops_list. Because the 2nd element is a percentage, you also need to either multiply the result by 0.01 or divide it by 100. In addition, note that the column 'Total Urban Population' should only be able to take on integer values. To ensure this, make sure you cast the output expression to an integer with int(). Create a scatter plot where the x-axis are values from the 'Year' column and the y-axis are values from the 'Total Urban Population' column.
'''

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], 
            df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int(tup[0]*tup[1]*.01) for tup in pops_list]

# Plot urban population data
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()
