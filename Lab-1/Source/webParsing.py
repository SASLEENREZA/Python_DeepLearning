import urllib.request
import bs4 as bs
import os
import csv
link = 'https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015'
source = urllib.request.urlopen(link).read()
soup = bs.BeautifulSoup(source, 'lxml')
print(soup.title.text)
table = soup.find('table')
table_rows = table.find_all('tr')
x = (len(table.findAll('tr')))
count = 0
with open('output1.csv', 'a') as f:
    while count<x:
        for tr in table_rows[1:x]:
            td = tr.find_all('td')
            row = [i.text for i in td]
            print(row)
            count = count +1
            row = str(row)
            f.write('\n')
            f.write(row)