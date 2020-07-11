# Functions
# Functions are a piece of reusable code
# It is used to perform a single task or a related set of actions

# -> Built in functions
# print
# sum
print(sum([10, 20, 30, 40, 50]))

# -> User defined functions
# Defining a user defined function
def fun():
    print('This is a function print statement')

# calling a user defined function
fun()

# -> return statement
print(fun())

def retfun():
    print('In the function')
    return 'Hello'

retfun()
print(retfun())

# functions with parameters
def paramfun(username):
    print('Hello ' + username)

paramfun('Alvyn')

def greeting(username):
    return 'Hello ' + username

print(greeting('Alvyn'))

# functions with more than 1 return variable
def more_parameters(a, b):
    return a, b

print(more_parameters(1, 2))

a, b = more_parameters(1, 2)
print(a)
print(b)

# functions with default parameters
def defaultparam(username='Alvyn'):
    return 'Hello ' + username

c = defaultparam()
d = defaultparam('Manohar')
print(c)
print(d)

# functions with parameters and default parameters
def mixedparameters(name, message='Good morning'):
    print(message + ' ' + name)

mixedparameters('Alvyn')

# variable length arguments
def fun(*var_tuple):
    for var in var_tuple:
        print(var)

fun('Alvyn', 23)

# scope of the variable => local variables, global variables
a = 5

def increment(a):
    a += 1
    print(a)
increment(20)

print(a)

def increment2():
    a += 1 # will return a error because a was not defined inside the function
    print(a)
# increment2()

def increment3():
    global a
    a += 1
    print(a)
    
print(a)

increment3()
# Recursion => PPT
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


# Blank function
def fun():
    pass

# End of the topic
# Assignment for this topic -> S2A7
# 1. Make a function for factorial. And print out this series (1! + 10) + (2! + 20) + (3! + 30) + (4! + 40) + ........
# 2. 
# 3. 
# 4. 
# 5. 
# Next Topic => Revision / PPTs