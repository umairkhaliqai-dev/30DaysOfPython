# In Python, web scraping is typically done using libraries. 
# The most common combination is requests (to download the webpage's HTML) 
# and BeautifulSoup (to parse the HTML and extract specific data).
# The process involves sending an HTTP request to a website's server,
# receiving the HTML content, and then navigating the HTML structure to find 
# and extract the information you need.
print()
# Example: Let's scrape the titles of all the quotes from the same website 
# and also find the author for the first quote. 
# This shows the two steps: getting the page and then parsing it to find 
# specific tags and attributes.

# 2_web_scraping_basics.py
import requests
from bs4 import BeautifulSoup

# 1. Send a request to the website
url = 'http://quotes.toscrape.com/'
print(f"Fetching data from: {url}")
response = requests.get(url)

# 2. Check if the request was successful (status code 200 means OK)
if response.status_code == 200:
    print("Successfully downloaded the webpage!")
    # 3. Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 4. Extract data: Find all quote divs
    all_quotes = soup.find_all('div', class_='quote')
    
    print(f"\n--- Scraped {len(all_quotes)} Quotes and Authors ---")
    for i, quote_div in enumerate(all_quotes, 1):
        # Inside each quote div, find the span with class 'text' for the quote
        quote_text = quote_div.find('span', class_='text').text
        # Inside the same div, find the small with class 'author' for the author
        author_name = quote_div.find('small', class_='author').text
        
        print(f"{i}. {quote_text} — {author_name}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

    print()
    
    # Pro tip is that to run any example regarding web scrapper must create 
    # venv and then intall pip beautifulsoup or any related lib, and then run code۔
# 1. IMPORT libraries
#       ↓
# 2. SEND request → Website
#       ↓
# 3. GET response (200 = OK)
#       ↓
# 4. PARSE HTML with BeautifulSoup
#       ↓
# 5. FIND all quote divs
#       ↓
# 6. LOOP through each quote
#       ↓
# 7. EXTRACT quote text
#       ↓
# 8. EXTRACT author name
#       ↓
# 9. PRINT formatted output
from bs4 import BeautifulSoup
import requests

# Your Amazon URL
url = "https://www.amazon.com/some-product-page"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# USE YOUR COPIED SELECTOR DIRECTLY!
selector = "#a-page > div.a-container.octopus-page-style > div.a-row.apb-browse-two-col-center-pad > div:nth-child(1) > div > div > div > h1 > b"

# Find the element
element = soup.select_one(selector)
print(element.text)  # Gets the text you want!
