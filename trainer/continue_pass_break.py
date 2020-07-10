# Task for Session 2
# continue and pass are used to skip out the running loop and move
# starting with continue
for i in range(10):
    if i % 2 == 1:
        continue
    print(i)


print()
# loop with pass
for i in range(10):
    if i % 2 == 1:
        pass
    print(i)


# NOTE: both the keywords will work similar but used differently. 
# Pass is only used when there is no other code to write in the block of code
# Continue is used when there are multiple lines of code
# Continue statement will not execute the code in a particular block
print()
# try out pass & continue on multiple lines of code

for i in range(10): 
    if i % 2 == 1:
        print(i)
        pass
        print(i)

for i in range(10):
    if i % 2 == 1:
        print(i)
        continue
        print(i)


# Assignment for this topic -> S2A1
# 1. Print  the specified series using continue statement -> (1/1) + 0 + (1/3) + (1/5) + (1/7) + (1/9) + ..... + (1/n), where n is defined by the user.
# Only the result should be printed
# 2. Print fibonaci series where user will specify n. if the user input is negative or floating point number break the loop
# 3. Print a series -> (1*2) + (2*3) - (3*4) + (4*5) - (5*6) + (6*7) - (7*8) + ...... + ((n-1)*n). Print only the result.
# Next Topic