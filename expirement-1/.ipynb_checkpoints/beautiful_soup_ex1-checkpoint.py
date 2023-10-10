from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Haze'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

title = soup.title.string
print(f"Title of the webpage: {title}")