
def Merge(colors1, colors2):
    a = colors1 | colors2
    return a
 
colors1 = { 'Black': 1, 'White': 2, }
colors2 = { 'Red': 3, 'Green': 4,}
print("Set 1 : ",colors1)
print("Set 2 : ",colors2)
Merge = (Merge(colors1, colors2))
print("Merge set : ",Merge)
