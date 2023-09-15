#change Element in tuple
x = ("apple", "grape", "orange")
print("Tuple=",x)
y = list(x)
y[1] = "banana"
x = tuple(y)
print("Chnage Element=",x)

#Adding Element in tuple
y.append("Kiwi")
x = tuple(y)

print("Add Element=",x)

#Delete Element
y.remove("apple")
x= tuple(y)

print("Delete Element",x)
