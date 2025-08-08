'''
    Write a program to double a given number and add two numbers using lambda ()
'''

double = lambda x: x * 2

num = 5
print("double of ",num," is: ",double(num))

add = lambda a,b: a + b

a = 5
b = 10
print("sum of",a,"and", b, "is: ",add(a,b))