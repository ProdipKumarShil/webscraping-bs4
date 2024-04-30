import csv
from bs4 import BeautifulSoup as bs
import requests

url = "http://books.toscrape.com/"

response = requests.get(url)
soup = bs(response.text, "html.parser")

h3_elements = soup.find_all('h3')

with open('data.csv', mode='w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow((['Text', 'Href']))
  
  for h3 in h3_elements:
    a_tag = h3.find('a')
    if a_tag:
      text = a_tag.text
      href = a_tag['href']
      
      writer.writerow([text, href])
      
      
      
print("Data Saved")