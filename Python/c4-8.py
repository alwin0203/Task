a=eval(input("Enter a list of numbers\n"))
c=a
b=len(c)
i=0
for i in range(0,b):
   d=c[i]%5
   if d==0:
       print(c[i])

