'''
In the function read_large_file(), read a line from file_object by using the method readline(). Assign the result to data. In the function read_large_file(), yield the line read from the file data. In the context manager, create a generator object gen_file by calling your generator function read_large_file() and passing file to it. Print the first three lines produced by the generator object gen_file using next().
'''

# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
    while True:

        # Read a line from the file: data
        data = file_object.readline()

        # Break if this is the end of the file
        if not data:
            break

        # Yield the line of data
        yield data
        
# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))
