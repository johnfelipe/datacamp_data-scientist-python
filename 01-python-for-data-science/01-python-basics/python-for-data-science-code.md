# The Python Interface
In the Python script on the below, you can type Python code to solve the exercises. If you hit Run Code or Submit Answer, your python script (script.py) is executed and the output is shown in the IPython Shell. Submit Answer checks whether your submission is correct and gives you feedback.

You can hit Run Code and Submit Answer as often as you want. If you're stuck, you can click Get Hint, and ultimately Get Solution.

You can also use the IPython Shell interactively by simply typing commands and hitting Enter. When you work in the shell directly, your code will not be checked for correctness so it is a great way to experiment.

Requirement(s)
- Experiment in the IPython Shell; type 5 / 8, for example.
- Add another line of code to the Python script: print(7 + 10).
- Hit Submit Answer to execute the Python script and receive feedback.
```
# Example, do not modify!
print(5 / 8)

# Put code below here
print(7 + 10)
```


# When to use Python?
Python is a pretty versatile language. For which applications can you use Python?

- [ ] - You want to do some quick calculations.
- [ ] - For your new business, you want to develop a database-driven website.
- [ ] - Your boss asks you to clean and analyze the results of the latest satisfaction survey.
- [x] - All of the above. 


# Any comments?
Something that Filip didn't mention in his videos is that you can add comments to your Python scripts. Comments are important to make sure that you and others can understand what your code is about.

To add comments to your Python script, you can use the # tag. These comments are not run as Python code, so they will not influence your result. As an example, take the comment on the right, # Just testing division; it is completely ignored during execution.

Requirement(s)
Above the print(7 + 10), add the comment # Addition works too.
```
# Just testing division
print(5 / 8)

# Addition works too
print(7 + 10)
```

# Python as a calculator
Python is perfectly suited to do basic calculations. Apart from addition, subtraction, multiplication and division, there is also support for more advanced operations such as:

Exponentiation: \**. This operator raises the number to its left to the power of the number to its right. For example 4\**2 will give 16.
Modulo: %. This operator returns the remainder of the division of the number to the left by the number on its right. For example 18 % 7 equals 4.

Requirement(s)
Suppose you have $100, which you can invest with a 10% return each year. After one year, it's $100 \times 1.1 = 110$ dollars, and after two years it's $100 \times 1.1 \times 1.1 = 121$. Add code on the right to calculate how much money you end up with after 7 years.
```
# Addition and subtraction
print(5 + 5)
print(5 - 5)

# Multiplication and division
print(3 * 5)
print(10 / 2)

# Exponentiation
print(4 ** 2)

# Modulo
print(18 % 7)

# How much is your $100 worth after 7 years?
print(100 * 1.1 ** 7)
```

# Variable Assignment
In Python, a variable allows you to refer to a value with a name. To create a variable use =, like this example:
x = 5
You can now use the name of this variable, x, instead of the actual value, 5.

Remember, = in Python means assignment, it doesn't test equality!
Requirement(s)
- Create a variable savings with the value 100.
- Check out this variable by typing print(savings) in the script.
```
# Create a variable savings
savings = 100

# Print out savings
print(savings)
```


# Calculations with variables
Remember how you calculated the money you ended up with after 7 years of investing $100? You did something like this:
100 * 1.10 ** 7
Instead of calculating with the actual values, you can use variables instead. The savings variable you've created in the previous exercise represents the $100 you started with. It's up to you to create a new variable to represent 1.10 and then redo the calculations!

Requirement(s)
- Create a variable factor, equal to 1.10.
- Use savings and factor to calculate the amount of money you end up with after 7 years. Store the result in a new variable, result.
- Print out the value of result.
```
# Create a variable savings
savings = 100

# Create a variable factor
factor = 1.1

# Calculate result
result = savings * factor ** 7

# Print out result
print(result)
```

# Other variable types
In the previous exercise, you worked with two Python data types:

int, or integer: a number without a fractional part. savings, with the value 100, is an example of an integer.
float, or floating point: a number that has both an integer and fractional part, separated by a point. factor, with the value 1.10, is an example of a float.
Next to numerical data types, there are two other very common data types:

str, or string: a type to represent text. You can use single or double quotes to build a string.
bool, or boolean: a type to represent logical values. Can only be True or False (the capitalization is important!).

Requirement(s)
- Create a new string, desc, with the value "compound interest".
- Create a new boolean, profitable, with the value True.
```
# Create a variable desc
desc = "compound interest"

# Create a variable profitable
profitable = True
```

# Guess the type
To find out the type of a value or a variable that refers to that value, you can use the type() function. Suppose you've defined a variable a, but you forgot the type of this variable. To determine the type of a, simply execute:
type(a)


# Operations with other types
Filip mentioned that different types behave differently in Python.

When you sum two strings, for example, you'll get different behavior than when you sum two integers or two booleans.

In the script some variables with different types have already been created. It's up to you to use them.

Requirement(s)
- Calculate the product of savings and factor. Store the result in year1.
- What do you think the resulting type will be? Find out by printing out the type of year1.
- Calculate the sum of desc and desc and store the result in a new variable doubledesc.
- Print out doubledesc. Did you expect this?
```
# Several variables to experiment with
savings = 100
factor = 1.1
desc = "compound interest"

# Assign product of savings and factor to year1
year1 = savings * factor

# Print the type of year1
print(type(year1))

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)
```

# Type conversion
Using the + operator to paste together two strings can be very useful in building custom messages.

Suppose, for example, that you've calculated the return of your investment and want to summarize the results in a string. Assuming the floats savings and result are defined, you can try something like this:

print("I started with $" + savings + " and now have $" + result + ". Awesome!")
This will not work, though, as you cannot simply sum strings and floats.

To fix the error, you'll need to explicitly convert the types of your variables. More specifically, you'll need str(), to convert a value into a string. str(savings), for example, will convert the float savings to a string.

Similar functions such as int(), float() and bool() will help you convert Python values into any type.

Requirement(s)

- Hit Run Code to run the code on the right. Try to understand the error message.
- Fix the code on the right such that the printout runs without errors; use the function str() to convert the variables to strings.
- Convert the variable pi_string to a float and store this float as a new variable, pi_float.
```
# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)
```

