# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'John'
greet = 'Helloworld!'
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

# Replace
# print(greet.replace('World', 'People'))

# Count
sub = 'H'
print(greet.count(sub))

# Starts with
print(greet.startswith('Hello')) # Returns a boolean

# Ends with
print(greet.endswith('World!')) # Returns a boolean

# Get length
# print(len(name))

# Split int a list
print(greet.split(' '))

# Find position
print(greet.find('o'))

# Is all alphanumeric
print(greet.isalnum())

# Is all alphabetic
print(greet.isalpha())