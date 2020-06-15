fruits = ["Apple","Banana","Orange","Banana","Mango"]
print(fruits)
print(fruits[-1])
print(fruits[1])
print(fruits[1:4])
print(fruits[1:])
print(fruits[:-3])
mixedlst = [1,"Apple",5.0,"Mango"]
print(len(fruits))

for f in fruits:
    #print (f)
    if f == "Banana":
        print("Banana is present")
        break

for f in range(len(fruits)):
    print(fruits[f])
    print(f)

fruits.append("Grapes")
print(fruits)
newfruits = fruits.copy()
print(newfruits)
newfruits.clear()
print(newfruits)
del newfruits
#print (newfruits)

print(fruits.count('Stawberry'))

a = [1,2,3]
b = [4,5]
a.extend(b)
c = a.copy()
print(a)
print(c)
veg = ["Onion","Carrot","Tomato"]
print(veg.index("Tomato"))
veg.insert(2,"Raddish")
print(veg)
veg.insert(2,"Beet Root")
print(veg)
veg.insert(-1,"Potato")
print(veg)

veg.pop(2)
print(veg)
veg.remove("Potato")
print(veg)

veg.reverse()
print(veg)
#decending order
veg.sort(reverse=True)
print(veg)
#ascending order
veg.sort()
print(veg)
