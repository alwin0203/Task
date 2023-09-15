#10.Implementing Web Scraping in Python with BeautifulSoup


from bs4 import BeautifulSoup
import requests
url = "https://infopark.in/companies/company/thrissur"
result = requests.get(url,verify=False)
print(result)
doc=BeautifulSoup(result.text)
print(doc)
#tags1=doc.find_all("h3",class_="company-name-hd")
tags2=doc.find_all("p")
#print(tags2)
#print(tags1)
#for company in tags1:
    #print(company.text)

for company in tags2:
    if "68" in company.get_text():
        print(company.text)
