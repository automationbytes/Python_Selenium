def SampleFunction():
    print("Hello World")

"""This is an
    example Function
    Here we will be
    using 3ple quotes"""

def exampleFunc():
    """This is an
    example Function
    Here we will be
    using 3ple quotes"""
    print(exampleFunc.__doc__)

SampleFunction()
exampleFunc()

def parameterfunction(name):
    print("Hi",name,"Welcome")

parameterfunction("Ram")
a = 10
def addNumbers(a,b):
    c = a+b
   # print(c)
    return c
addNumbers(5,3)

def recursion_factorial(x):
    if x==1:
        return 1
    else:
        return(x*(recursion_factorial(x-1)))
number=4
print("The factorial of",number,"is",recursion_factorial(number))

def rec(x):
    if x == 1:
        return 1
    else:
        return (x*(rec(x-1)))

print(rec(int(4)))
