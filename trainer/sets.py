# Sets
# Sets are a randomly ordered group of sequences seperated by a symbol , and enclosed inside the {} parathensis
# List are mutable

# -> Defining empty set
# There is only one way to do this
a = {}
print(a)
# -> Defining a set of a single data
b = {2}
print(b)
c = set([1])
print(c)

# -> Defining a set of multiple data
d = {2, 3, 4, 14, 6, 99, 87, 54, 22, 11}
print(d)
e = set([2, 3, 4, 14, 6, 99, 87, 54, 22, 11])
print(e)
# -> Print and look on the order of the set we have defined
# we have already seen that the data was not in order we defined. Just have a look carefully
print({2, 24, 14, 36, 22, 11, 14, 45, -7, -12, -1, 101, 6})

# -> Defining set of mixed types
# Note we can only store numbers or strings or tuples in sets and not lists
f = {(2, 4), 4, 5, 7, -2, 'Hi', 'Hello'}
print(f)
# g = {[4, 2], 1, 2} # It will give error BUT SHOULD BE SHOWN TO THE STUDENTS

# -> adding new data to a set
f.add(5)
print(f)

# -> find the length
length = len(f)
print(length)

# End of the Topic
# Assignment for this topic -> S2A5
# 1. 
# 2. 
# 3. 
# Next Topic