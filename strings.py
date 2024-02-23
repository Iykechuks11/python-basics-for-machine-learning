# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'John'
age = 28

# Concatenate
# print('Hello, my name is', name, 'and I am', age, 'years old.')


# String Formatting

# Or Auguments by position
# print('My name is {name} and I am {age} years old.'.format(name=name, age=age))

# F-Strings (3.6+)
# print(f'Hello, my name is {name} and I am {age} years old')


# String Methods
# Capitalization
# print(name.capitalize())

# Make all uppercase
# print(name.upper())

# Make all lowercase
# print(name.lower())

# Swap case - If a letter is upper, it makes it lower, if it is lower it makes it upper, and repeats this for all the letters
print(name.swapcase())

# Get length
print(len(name))