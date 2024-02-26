# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create a dictionary
person = {
    'first_name': 'John',
    'last_name': 'Testimony',
    'age': 28
}

# print(person, type(person))

# Using a constructor
person2 = dict(
    first='Sam',
    last='WIlliams'
)

# print(person2, type(person))

# Get values
print(person['first_name'])
print(person.get('last_name'))

# Add values
person['phone']=111222

# Get dict key
print(person.keys())

# Get values
print(person.values())

# Length of a dictionary
print(len(person))

# Remove values
# del(person['age'])
deleted = person.pop('age')
print(deleted)

# Copy dict
# person2 = person.copy()
person2.update(person)


print(person2)
