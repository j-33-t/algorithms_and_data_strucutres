
# 1. Accessing List/Array

## Create list / array (Sorted List)
from unicodedata import numeric


new_list = [1,2,3,5,6,7,8,9,10]

## Access a specific element in a list/array
result = new_list[0]

## Show specific element
result

## Linear Search in a list

### Using if
if 10 in new_list:
    print(True)

### Using for loop
for n in new_list:
    if n == 1:
        print(True)
        
        break
    

# 2.  Appending List/Array
numbers = []
len(numbers)

# appending
numbers.append(2)
numbers.append(200)
        
numbers

# Extending list
numbers.extend([4,5,6])
numbers

# 3. Deleting elements
numbers.remove(6)
numbers
