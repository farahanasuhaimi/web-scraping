from bs4 import BeautifulSoup
import requests

# Define the URL
url = 'http://quotes.toscrape.com/'

# Send an HTTP GET request
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find and scrape the tags
tags = soup.select('.tag-item a')
tag_list = [tag.get_text() for tag in tags]

# Print the list of tags
print("List of tags:")
for tag in tag_list:
    print(tag)
