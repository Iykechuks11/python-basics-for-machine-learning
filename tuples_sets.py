# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create a new Tuple
fruits = ('Apples', 'Oranges', 'Grapes')

# Use a constructor
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

fruits3 = ('Apples',)

print(fruits[0]) # First value
print(len(fruits2))
print(fruits3, type(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.
fruits_set = {'Apples', 'Oranges', 'Grapes'}

# Check if in the set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Mangoes')

# Remove from set
fruits_set.remove('Apples')

# Add duplicate. When you add an already existing item to a set, nothing changes.
fruits_set.add('Oranges')

# Clear the set
# fruits_set.clear()

# Delete the set
# del fruits_set

print(fruits_set)