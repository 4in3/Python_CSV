import urllib.request
import csv
from bs4 import BeautifulSoup

url = urllib.request.urlopen("https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm")

soup = BeautifulSoup(url,'html.parser')

newfile = 'data.csv'

csv_writer = csv.writer(open(newfile,'w'))

data = []

for tr in soup.find_all('tr'):
    for td_date in tr.find_all('td', attrs={'class':'B6'}):
        for td_price in tr.find_all('td', attrs={'class':'B3'}):
            data.append([td_date.text, td_price.text])
    

#two collumns date and price
for item in data:
    csv_writer.writerow(item)
