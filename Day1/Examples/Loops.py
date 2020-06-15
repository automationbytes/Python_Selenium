#For Loop

#for varname in range (start,stop,step) : start=0; step=1
for i in range(10,101,5):
    print (i)

for j in range(10):
    print (j)

for p in range(2,10,2):
    print (p)

str = "India"
for s in str:
    print (s)

for g in range(len(str)):
    #print(g)
    print(str[g])

#WHile statements

x = 10
while x<0: # condition
    print(x)  # statements
    x = x + 5
else:
    print("Execution completed")

