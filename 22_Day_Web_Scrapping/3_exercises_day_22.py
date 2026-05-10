# Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
import requests
from bs4 import BeautifulSoup
import json

# 1. Fetch the webpage
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
print(f"Fetching data from: {url}")
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raise an error for bad status codes (4xx or 5xx)
    print("Successfully downloaded the webpage!")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching the page: {e}")
    exit()

# 2. Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')
print("=" * 50)
print("DEBUG: First 2000 characters of webpage")
print("=" * 50)
print(soup.prettify()[:2000])  # Shows first 2000 chars of HTML
print("=" * 50)

headings = soup.find_all(['h1', 'h2', 'h3', 'h4'])
print("All headings found:")
for h in headings[:10]:  # First 10 headings
    print(f"  {h.name}: {h.text.strip()[:50]}")

# 3. Extract Data
bu_facts = {}

# --- Helper function to clean text ---
def clean_text(text):
    return text.strip().replace('\n', ' ').replace('\r', ' ').replace('  ', ' ')

# --- Extract "Quick Facts & Stats" section ---
quick_facts = {}
# Find the section based on the provided HTML structure
# Look for the heading "Quick Facts & Stats" and then find adjacent data
quick_facts_section = soup.find('h3', string='Quick Facts & Stats')
if quick_facts_section:
    # The data is in sibling or nearby divs with class 'fact-box'
    for fact_box in quick_facts_section.find_next_siblings('div', class_='fact-box'):
        title_elem = fact_box.find('h3')
        value_elem = fact_box.find('div', class_='fact-box-value')
        if title_elem and value_elem:
            title = clean_text(title_elem.text)
            value = clean_text(value_elem.text)
            quick_facts[title] = value

bu_facts['quick_facts'] = quick_facts

# --- Extract "Community" section ---
community_data = {}
community_section = soup.find('h3', string='Community')
if community_section:
    # Look for the unordered list that follows this heading
    ul_list = community_section.find_next_sibling('ul')
    if ul_list:
        for li in ul_list.find_all('li'):
            # Split the text into key and value (e.g., "Student Body 37,557")
            text = clean_text(li.text)
            # Find where the number or key phrase starts
            parts = text.split(' ', 1)
            if len(parts) == 2:
                key, value = parts
                community_data[key] = value

bu_facts['community'] = community_data

# --- Extract "Campus" section ---
campus_data = {}
campus_section = soup.find('h3', string='Campus')
if campus_section:
    # Similar structure: 'fact-box' divs
    for fact_box in campus_section.find_next_siblings('div', class_='fact-box'):
        title_elem = fact_box.find('h3')
        value_elem = fact_box.find('div', class_='fact-box-value')
        if title_elem and value_elem:
            title = clean_text(title_elem.text)
            value = clean_text(value_elem.text)
            campus_data[title] = value

bu_facts['campus'] = campus_data

# --- Extract "Academics" section ---
academics_data = {}
academics_section = soup.find('h3', string='Academics')
if academics_section:
    ul_list = academics_section.find_next_sibling('ul')
    if ul_list:
        for li in ul_list.find_all('li'):
            text = clean_text(li.text)
            parts = text.split(' ', 1)
            if len(parts) == 2:
                key, value = parts
                academics_data[key] = value

bu_facts['academics'] = academics_data

# 4. Save to JSON file
output_filename = 'bu_facts_stats.json'
try:
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(bu_facts, f, indent=4, ensure_ascii=False)
    print(f"\nData successfully saved to '{output_filename}'")
except IOError as e:
    print(f"An error occurred while saving the file: {e}")

# 5. (Optional) Print a preview of the data
print("\n--- Preview of Extracted Data ---")
for section, data in bu_facts.items():
    print(f"\n{section.replace('_', ' ').title()}:")
    if data:
        for key, value in list(data.items())[:3]:  # Show first 3 items per section
            print(f"  {key}: {value}")
        if len(data) > 3:
            print(f"  ... and {len(data) - 3} more items.")
    else:
        print("  No data extracted for this section.")

        print()
        print()
# Core Pattern to Remember (Just 5 Steps):
# Download webpage = requests.get(url)

# Parse HTML = BeautifulSoup(response.text)

# Find heading = soup.find('h3', string='Heading Text')

# Find data = .find_next_siblings() or .find_all('li')

# Save as JSON = json.dump()

# That's it! Everything else is just repeating these patterns.
####this entire above code is for just explaining the structure of how to scrap a websit 
#this is a sample excersice with no real data extraction successful as the tag info may hasve been changed.
