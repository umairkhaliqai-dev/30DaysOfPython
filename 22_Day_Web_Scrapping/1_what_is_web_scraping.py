# Web scraping is an automated method used to extract large amounts of data from websites. 
# The data on websites is in HTML format.
# web Scr helps convert this unstru data into a stru form (CSV file/database) can be analyz/stored. 
# It's like a digital copy-paste or a "bot" reading a website.
## Example: Imagine you want to get a list of all the blog post titles from a news website. 
## Instead of manually copying each title one by one.
## you can write a Python script (web scraper) that visits the website.
## grabs all the text inside the tags (which often contain titles).
## prints them out or saves them to a list.
# 1_what_is_web_scraping.py
import requests
from bs4 import BeautifulSoup

# A basic conceptual example
url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all elements with the tag 'span' and class 'text' (which contains quotes)
quotes = soup.find_all('span', class_='text')

print("--- Scraping Quotes ---")
for quote in quotes[:3]: # Print first 3 quotes as a sample
    print(f"Quote: {quote.text}")
print("\nThis is a simple example of extracting (scraping) specific data from a webpage.")

print()
# so to run this above commands for web scrapping we need to create web scrapping venv 
# python3 -m venv web_scraping_env
# source web_scraping_env/bin/activate
# pip install requests beautifulsoup4
# then run the command of sript given 
# when done then type deactivate to remove venv. 
### cd "/home/umair/Python.pyFile-01-04-26" && python3 -m venv venv && source venv/bin/activate && pip install requests beautifulsoup4
