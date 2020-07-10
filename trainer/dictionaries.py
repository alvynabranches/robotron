# Dictonary
# Dictonary are multiple values of key-value pair
# Dictonary are mutable

# -> Defining an empty dictonary
a = {}
print(type(a))
print(a)
b = dict()
print(type(b))
print(b)

# -> Defining a dictonary with single key-value pairs
c = {'name': 'Alvyn Abranches'}
print(c)
d = dict(name='Alvyn Abranches')
print(d)

# -> Defining a dictonary with multiple key-value pairs
e = {'firstname': 'Alvyn', 'lastname': 'Abranches'}
print(e)
f = dict(firstname='Alvyn', lastname='Abranches')
print(f)

# -> Defining mixed datatype for value
g = {'name': 'Alvyn Abranches', 'age': 23, 'height':6.2}
print(g)
h = {'name': ['Manoj', 'Rajesh', 'Promod'], 'age': [26, 32, 42], 'height': (5.10, 5.8, 6.)}
print(h)

# -> Defining mixed datatype for key
# NOTE: Supported types are only strings, numbers
i = {1: 'Hello', 2.25: 'This', 'word': 'is', 'word2': 'an example'}
print(i)

# -> Nested dictonaries
j = {'name': {'firstname': 'Promod', 'lastname': 'Sawant'}, 'age': 42}
print(j)

# -> List as value in a dictonary
# we have seen this above

# -> finding the length of a dictonary
length = len(j)
print(length)

# -> iterating over a dictonary
for z in g:
    print(z) # this prints out the keys

for z in g:
    print(g[z])

# -> adding new data to a existing dictonary
print(g)
g['weight'] = 65
print(g)

# -> iterating over a dictonary nested with another dictonary
print(j)
print(j['name']['firstname'])

# -> other methods
print(g.values()) # displays all the values
print(g.get('name'))
print(g.items())

# End of this topic
# Assignment for this topic -> S2A6
# 1. make a dictonary with your name, age, school name, and other details and print it out.
# 2. make a dictonary of roll no and name of your classmates. Each one should hold a list. eg -> rollno = [7, 22, 25, 29], 
#    but it should be a directory. Display the results
# 3. make a dictonary to store your subjects and marks of those subjects you got in the previous exam. Print the results.
# 4. 
# 5. 
# Next topic