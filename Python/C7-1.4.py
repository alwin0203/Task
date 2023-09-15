emp_dict = {'Name': 'Alwin','ID': 1}

try:
    emp_role=emp_dict['Role']
    print(emp_role)
except:
    print("Key Error!!!!")
