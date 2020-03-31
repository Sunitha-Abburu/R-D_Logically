import requests
import csv
from bs4 import BeautifulSoup as bp

url = 'https://www.emdat.be/classification'
res = requests.get(url)
soap = bp(res.text, 'html.parser')
a = []
rows = soap.find_all('tr')
data = []
for row in range(len(rows)):
    team_row = []
    columns = rows[row].findAll('td')
    for column in columns:
        team_row.append(column.getText())
    if len(team_row) == 4:
        data.append(team_row)
    else:
        d1 = []
        m = 4 - len(team_row)
        for i in range(0, m):
            d1.append('NONE')
        d1 = d1 + team_row
        data.append(d1)

with open('filename.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)
