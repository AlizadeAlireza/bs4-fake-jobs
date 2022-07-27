import requests
from bs4 import BeautifulSoup
import xlsxwriter


URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.text, "html.parser")

results = soup.find(id="ResultsContainer")

jobs_sections = soup.find_all('div', class_='card-content')


'''for sec in jobs_sections:
    print(sec.text)'''
# Create a workbook and add a worksheet
workbook = xlsxwriter.Workbook('Jobs.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

for sec in jobs_sections:
    title = sec.find("h2", class_='title')
    company = sec.find("h3", class_='company')
    location = sec.find("div", class_='location')
    if None in (title, company, location):
        continue
    worksheet.write(row, col, title.text)
    worksheet.write(row, col+1, company.text)
    worksheet.write(row, col+2, location.text)

    row+=1 
workbook.close()
print("amir mohammad goli")
