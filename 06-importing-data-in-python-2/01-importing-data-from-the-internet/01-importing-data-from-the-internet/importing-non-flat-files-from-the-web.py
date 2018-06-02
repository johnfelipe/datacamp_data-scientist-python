'''
Assign the URL of the file to the variable url. Read the file in url into a dictionary xl using pd.read_excel() recalling that, in order to import all sheets you need to pass None to the argument sheetname. Print the names of the sheets in the Excel spreadsheet; these will be the keys of the dictionary xl. Print the head of the first sheet using the sheet name, not the index of the sheet! The sheet name is '1700'
'''

# Import package
import pandas as pd

# Assign url of file: url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file: xl
xl = pd.read_excel(url,sheetname=None)

# Print the sheetnames to the shell
print(xl.keys())

# Print the head of the first sheet (using its name, NOT its index)
print(xl['1700'].head())
