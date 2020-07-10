# Tuples
# Tuples are a group of sequences seperated by a symbol , and enclosed inside the () parathensis
# Tuples are unmutable

# -> Defining a empty tuple 
a = ()
print(type(a))
b = tuple()
print(type(b))

# -> Defining a tuple with single data
c = (1,)
print(c)

# -> Defining a tuple with multiple data
d = (10, 12, 15, 25, 35)
print(d)

e = (1.2, 25.20, 19.55, 45.32)
print(e)

# -> Unmutablity
# e[1] = 5 -> This code will give an error BUT SHOULD BE SHOWN TO THE STUDENTS

# -> Finding length of the tuple
length = len(e)
print(length)

# -> Indexing
print(e[2])
print(e[0])
print(e[-1])

# -> Iterating over a tuple
for i in range(len(e)):
    print(e[i])

for element in e:
    print(element)

# -> tuple with mixed datatype
f = (10, 1.25, "Hello")
print(f)

# -> nested tuples
g = ((1, 2), (5, 6), (9, 10))
print(g)

# End of this topic
# Assignment for this topic - S2A3
# 1. Make a new tuple adding .25 to a existing tuple of integers or float
# 2. Make a new tuple finding the length of the existing tuple of string
# 3. 
# Next Topic