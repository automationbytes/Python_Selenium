a = 10
b = 15
c = 20

if a>b: #a<b is the condition
    print("B is greater") #this is the statemtnt

if a>b:
    print("A is greater than B")
elif a>c:
    print("A is greater than c")
else:
    print("A is lesser than B and C")

#Biggest of 3 numbers

a = 10
b = 25
c = 200
d = 400

if a>b and a>c and a>d: #F and F
    print ("A is largest")
elif b>a and b>c and b>d: #T and T
    print ("B is largest")
elif c>a and c>b and c>d:
    print("C is largest")

else:
    print("D is largest")

a = 10
A = "10.00"
print (A)
print (a)