'''
Import the function urlretrieve from the subpackage urllib.request. Assign the URL of the file to the variable url. Use the function urlretrieve() to save the file locally as 'winequality-red.csv'
'''

# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally
urlretrieve(url,'winequality-red.csv' )


# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())
