
from bs4 import BeautifulSoup
import requests
url = "https://infopark.in/companies/company/thrissur"
result = requests.get(url,verify=False)
print(result)
doc=BeautifulSoup(result.text,"html.parser")
tags1=doc.find_all("h3",class_="company-name-hd")
for company in tags1:
    print(company.text)
    a=open('myfile.txt','a')
    a.write(company.text)
    a.write("\n")
    a.close()
    a=open('myfile.txt','r')

