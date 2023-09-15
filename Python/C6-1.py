#1.create a student file

f=open("file1.txt","w")

f.write("Student name : ")
f.write("Stud 10 : ")
f.write("Dob : 02/02/2015")
f=open("file1.txt","r")
print(f.read())
f.close()
