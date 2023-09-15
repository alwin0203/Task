colors1 = { 'Black': 5, 'White': 2, 'Pink': 4}
colors2 = { 'Red': 1, 'Green': 3, 'Brown': 6}
print("Set 1 : ",colors1)
print("Set 2 : ",colors1)
concatenate = {}
for d in (colors1, colors2,): concatenate.update(d)
print("concatenate set : ")
print(concatenate)
