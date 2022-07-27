import requests
from bs4 import BeautifulSoup
import xlsxwriter
import re

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")
def jobs():
    jobs_1 = soup.find_all('h2', class_="title")
    print("our job list: ")
    print()
    for job in jobs_1:
        print(job.string)

def location():

    print("our job's location:\n")
    print()    
    locations = soup.find_all('p', class_="location")
    for location in locations:
        print(location.text.strip())
def workers():
    print("our job's workers:\n")
    workers = soup.find_all('h3', class_="subtitle")

    for worker in workers:
        print(worker.string)
def links():
    links = soup.find_all('a', string= "Apply")
    for link in links:
        print(link.get('href'))
#print(soup.find("footer", class_="card-footer"))
#print(soup.find("a").next_sibling.next_sibling)

# Create a workbook and add a worksheet
workbook = xlsxwriter.Workbook('Jobs.xlsx')
worksheet = workbook.add_worksheet()

jobs_1 = soup.find_all('h2', class_="title")
row = 0
col = 0
location()