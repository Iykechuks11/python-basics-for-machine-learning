# A List is a collection which is ordered and changeable. Allows duplicate members.

subjects = ['ML', 'SL', 'AC',]

# Using a constructor
numbers = list((1, 2, 3, 4, 5))

# Default
# numbers2 = [1, 2, 3, 4, 5]
# print(numbers2)

# print(numbers)
# print(type(subjects))
# print(len(subjects))

# Get a value
print(subjects[0])

# Apend to list
subjects.append('Turkish')

# Remove
subjects.remove('ML')

# Insert into position
subjects.insert(1, 'Macedonia')

# Remove with pop
subjects.pop(0)

# Sort list
subjects.sort()

# Reversed list
subjects.reverse()

print(subjects)