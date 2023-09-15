a = (4, 5, 4, 5, 6, 6, 5, 5, 4)


print("Tuple : " + str(a))

res = dict()
x=list(a)
y=[]
for i in x:
	if i not in y:
		y.append(i)
for i in y:
	res[i]=x.count(i)

print("Tuple elements frequency is : " + str(res))
