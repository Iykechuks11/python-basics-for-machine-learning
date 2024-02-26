# If/ Else conditions are used to decide to do something based on something being true or false
x = -10
y = 10


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

if x > y:
    print(f'{x} is greater than {y}.')
elif x < y:
    print(f'{y} is greater than {x}')
else:
    print(f'{y} is equal to {x}.')


# Logical operators (and, or, not) - Used to combine conditional statements
# and
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')

# not
if not x > 1:
    print(f'{x} is negative')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1, 2, 3, 4, 5, 10]

# in
if y in numbers:
    print(f'{y} is in number list')

if x not in numbers:
    print(f'{x} is not in the number list')


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
