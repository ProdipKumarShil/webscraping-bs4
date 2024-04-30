from bs4 import BeautifulSoup as bs
import requests
import csv

# visite and get website 
url = "http://books.toscrape.com/"
response = requests.get(url)
soup = bs(response.text, "html.parser")

# get all the urls
book_urls = []
for article in soup.find_all('article'):
  book_url = article.find('a')['href']
  book_urls.append(url + book_url)

with open('book_data.csv', mode='w', newline='', encoding='utf-8') as file:
  writer = csv.writer(file)
  writer.writerow(["Title", "Price", "Availability", "Link"])
  
  for book_url in book_urls:
    book_response = requests.get(book_url)
    book_soup = bs(book_response.text, "html.parser")
    
    title = book_soup.find("h1").text.strip()
    price = book_soup.find("p", class_="price_color").text.strip()
    availability = book_soup.find('p', class_="instock availability").text.strip()
    
    writer.writerow([title, price, availability, book_url])
    
    
print("data Saved")
