from bs4 import BeautifulSoup
import requests
import openpyxl

url = "https://plaksha.edu.in/team/founding-group/founders-&-trustees"
workbook = openpyxl.load_workbook("founders.xlsx")
worksheet = workbook.active

heading_row = ['Name', 'Current Position', 'Education', 'Bio']
worksheet.append(heading_row)

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")

team_boxes = soup.find_all("div", class_="TeamBox")

for prof in team_boxes:
    prof_data = []
    name = prof.find("h3").text
    link = prof.find("a")["href"]

    # Visit each link
    response = requests.get(link)
    link_content = response.content

    link_soup = BeautifulSoup(link_content, "html.parser")

    # Find divs with class "InfoRow" and extract the text
    info_rows = link_soup.find_all("div", class_="InfoRow")
    prof_data.append(name)
    for info_row in info_rows:
        for row in info_row:
            if row.name == "span":
                prof_data.append(row.text.strip())
    
    # add bio
    bio_info = link_soup.find("div", class_="BioInfo")
    for row in bio_info:
        if row.name == "p":
            prof_data.append(row.text.strip())
    
    # add to excel sheet
    worksheet.append(prof_data)

workbook.save("founders.xlsx")