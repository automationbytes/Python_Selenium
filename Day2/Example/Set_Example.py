fruits = {"Orange","Apple","Banana","Orange"}
print(fruits)

fruits.add("Watermelon")
print(fruits)

new_fruits = fruits.copy()
print(new_fruits)
new_fruits.clear()
print(new_fruits)
del new_fruits

a = {"Orange","Apple","Mango","Watermelon"}
b = {"Apple","Google","Microsoft","Orange"}
print(a.difference(b))
print(a.union(b))
print(a.intersection(b))
print(a.symmetric_difference(b))

veg = {"Onion","Carrot","Tomato","Potato"}
v = {"Carrot","Potato"}

newveg = veg.copy()
print(veg)
print(newveg)
print(veg.isdisjoint(fruits))

print(v.issubset(veg))
print(veg.issuperset(v))

country = {"India","US","UK"}
add_con = {"Aus","SA"}
country.update(add_con)
print(country)

