# Task for Session 2
# Strings
# -> Defining a string with single quote
a = 'Hello World'
print(a)

# -> Defining a string with double quotes
b = "Hello World"
print(b)

# when to use single quotes and double quotes
# c = 'It's' Saturday today' # this line will be giving a error but have to show them
c = "It's Saturday today"
print(c)
# d = "Biography of "Steve Jobs"" # this line will give an error BUT HAVE TO BE SHOWN TO THE STUDENTS
d = 'Biography of "Steve Jobs"'
print(d)

# -> Defining a multiline single quote string
e = """Hello Students,
This is a Python Programming class.
and this is a example of multi-line single quote string
"""
print(e)

# -> Defining a multiline double quote string
f = '''Hello Students,
This is a Python Programming class.
and this is a example of multi-line single quote string'''
print(f)

# -> Indicing a string
# NOTE: Index starts from 0 and -1 for the last item in Python for everything
a = 'Hello World'
print(a[0])
print(a[-1])
print(a[3])
print(a[5])

# String Concatenation -> Joining two strings together using + operator
s1 = "Hello"
s2 = "World"
s3 = s1 + s2
print(s3)

s3 = s1 + ' ' + s2
print(s3)

# Replication / Repeatation -> Copying the same string another time
s4 = s3 * 3
print(s4)

# Slicing a String -> showing only some part of the string
print(s3[2:10])
print(s3[2:])
print(s3[:5])
print(s3[5:-1])
# Find the length of the string -> len()
length = len(s3)
print(length)

# \n and \t
s5 = s3 + '\n' + s3
print(s5)
s6 = s3 + '\t' + s3
print(s6)

# f string
print(f'This is s1 variable : {s1}, and this is s2 variable {s2}')

# r string
print(r'This is a raw string \n')

# End of this topic
# Assignment for this topic -> S2A2
# 1. You will have to input the name of the user, after the enter button is pressed you have to output a message hello and the user name
# 2. Using f string you have to print a pattern
# |   *   |
# |  ***  |
# | ***** |
# |*******|
# This will be the pattern, n number of lines will be decided by the user.
# 3. Concatenate a two strings, first one as it is, and 2nd one replicated by 5
# Next Topic