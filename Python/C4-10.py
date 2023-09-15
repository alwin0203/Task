nums = [2, 3, 12, 20, 33, 51, 60, 63]

even = []
odd = []

for i in nums:
    if(i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)
        
print("Even Numbers List: ",even)
print("Odd Numbers List: ",odd)
