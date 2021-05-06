# Getting user input
math_score = int(input("What's your math score(0-100): "))
physics_score = int(input("What's your pyhsics socre(0-100): "))
comment = str(input("Anything want to metion? "))

# types of print
print('math_score:',math_score, end = ' ,')
print('physics_score:', physics_score)
print(comment)

print('This is string :', comment, 'This is number :' ,math_score, physics_score)

print('This is string :' + comment, 'This is number :', math_score + physics_score)

#The way to print multiple items
print('{1} and {0}'.format('spam', 'eggs'))
str1='str1'; num1=1; num2=2; num3=3; num4=4
print('{0} {1} %d {2} {3} %s'.format('test','11',num1,num2)%(num3,str1))
#


import time
# store start time 
start = time.time()

# Running codes

# Calculate the running time
print("time: ", time.time() -start)


#Variadic Parameters(*)
def print_names(*args, **kwargs):
    print(args)
    print(kwargs)

print_names('richard', 'daniel', A ='okyong')

