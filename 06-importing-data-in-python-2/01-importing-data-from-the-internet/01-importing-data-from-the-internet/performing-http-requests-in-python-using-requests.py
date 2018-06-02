'''
Import the package requests. Assign the URL of interest to the variable url. Package the request to the URL, send the request and catch the response with a single function requests.get(), assigning the response to the variable r. Use the text attribute of the object r to return the HTML of the webpage as a string; store the result in a variable text. Hit submit to print the HTML of the webpage.
'''

# Import package
import requests

# Specify the url: url
url = 'http://www.datacamp.com/teach/documentation'

# Packages the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response: text
text = r.text

# Print the html
print(text)
