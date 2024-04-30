# from bs4 import BeautifulSoup
# import requests

url = "http://books.toscrape.com/"
# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")

# h3_elements = soup.find_all('h3')
# link_texts = []
# for h3 in h3_elements:
#   a_tag = h3.find('a')
#   link_texts.append(a_tag.text.strip())

# print(link_texts)

from bs4 import BeautifulSoup as bs
import requests

response = requests.get(url)
soup = bs(response.text, "html.parser")

h3_elements = soup.find_all('h3')

print("Total ", len(h3_elements), "books found!!")
for h3 in h3_elements:
  a_tag = h3.find('a')
  if a_tag:
    print("Name: ", a_tag.text)
    print("Link: ", url + a_tag["href"], '\n\n')
  else:
    print("Not Found!!")
