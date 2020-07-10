# List
# Lists are a group of sequences seperated by a symbol , and enclosed inside the [] parathensis
# List are mutable

# -> Defining a empty list
a = []
print(a)
b = list()
print(b)

# -> Defining a list with single data
c = [5]
print(c)

# -> Defining a list with multiple data
d = [5, 12, 124, 234, 456, 789]
print(d)
e = [2.5, 5.5, 12.5, 35.5, 12.003]
print(e)
f = ["Hello", 'How', 'are', 'you', '?']
print(f)

# -> Defining a mixed type list
g = [5, 12, 124, 2.5, 5.5, 12.5, 'Hello', 'How', 'are', 'you', '?']
print(g)

# -> Nested Lists
h = [5, 12, 124, 2.5, 5.5, 12.5, 'Hello', 'How', 'are', 'you', '?', [234, 456, 789], d, e, f]
print(h)

# -> List with a tuple
i = [5, 12, 124, (2.5, 5.5, 12.5), 'Hello', 'How', 'are', 'you', '?', [234, 456, 789], d, e, f]
print(i)

# -> finding the length of the list
length = len(i)
print(i)

# -> iterating over a list
for z in range(len(f)):
    print(f[z])

for element in f:
    print(element)

# -> adding new data to a list
print(f)
f.append('New Element Here')
print(f)

# -> adding a new data before a certain index
print(f)
f.insert(0, 'New Element before the 0 index')
print(f)

# -> remove a element with a specific value
print(d)
d.remove(5)
print(d)

# -> remove a element at a particular index
print(i)
i.pop(0)
print(i)

# -> sorting a list by values
print(f)
f.sort()
print(f)

# NOTE: 
# 1. sorting a list with tuples or lists inside will give you error
# 2. sorting a list with (str and integer), (str and float) will give an error 

print(d)
print(e)
j = d + e
print(j)
j.sort()
print(j)

# -> reverse all the element of a list
k = e + d
print(k)
k.reverse()
print(k)

# -> Slicing a list => showing only specific elements
print(i[2:5])
print(i[2:])
print(i[:4])

# -> List comprehesion
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# now we want y to be x**2
# just writing x**2 wont do the job, so we need to do it element wise
# the other approach to do this is iterating but instead we can use which can be done in a single line

# previously used for loop for iteration
y = []
for element in x:
    y.append(element**2)

print(x)
print(y)

# instead we can try list comprehension
# we have already defined x, now we will define y as x**2
y = [element**2 for element in x]
print(y)

# -> More with List comprehension


# End of this topic
# Assignment for this topic -> S2A4
# 1. Accessing Elements from lists (remember the indicing method used in strings)
# 2. Print out every element of a list in reverse order
# 3. For a list of integers add 5 to every element. Use list comprehension
# 4. For a list of integers add all the elements of it. Print out the answer only.
# 5. For a list of string concatenate up it with another list of string.
# Next topic