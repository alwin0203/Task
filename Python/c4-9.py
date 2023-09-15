total = 0
list1 =eval (input("Enter A List Of Numbers\n"))

for ele in range(0, len(list1)):
	total = total + list1[ele]

print("Sum of all elements in given list: ", total)
