#Arthimetic Operators
'''Arithmetic operators are used to perform arithmetic operations between two operands. It includes +(addition), - (subtraction), *(multiplication),
 /(divide), %(reminder), //(floor division), and exponent (**).
 '''

a = 5
b = 2
print (a+b)
print (a-b)
print (a*b)
print (a/b) # real division value
print (a%b) # remainder value
print (a**b) #power of - a^b 5^2
print (a//b) # quoitent value
#here a, b called as operands and + symbol is called as operator

#Comparison Operators
''' Comparison operators are used for comparing the value of the two operands and returns boolean true or false accordingly. 
'''

x = 15
y = 10

print (x == y) #to check equality ie 15 = 10
print (x!=y) #Non equality
print(x<y) #less than
print (x>y) #greater than
print (x>=y) #greater than or equalto
print (x<=y) #less than or equalto

#Assignment Operators
#The assignment operators are used to assign the value of the right expression to the left operand.

x = 10 # = assignment == to check the equality
p = 5
q = 3
p += q # p = p+q
print (p) #8
p -=q
print (p)


#Logical Operators
    #The logical operators are used primarily in the expression evaluation to make a decision. Python supports the following logical operators.

x = 10
y = 5
z = 15

if (x+y and z) == 15:
    print ("The value is equals to 15")
else:
    print("Value not equal")

    #T and T - T
    #T and F - F
    #F and T - F
    #F and F - F
#OR statements

if (x+y or z) == 15:
    print ("Atleast one value is equals to 15")
else:
    print("Value not equal")

# T or T = T
# T or F = T
# F or T = T
# F or F = F

#membership operator
print ("a" in "India")  # True
print ("b" not in "India")  # True
string = "India"
print(isinstance(string,float))
#identity operators
a = "India"
b = "india"
print (a == b)
print (a is b)
print (a is not b)