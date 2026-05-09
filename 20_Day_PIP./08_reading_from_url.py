  # You can use Python packages (like requests or urllib) to fetch data directly from a web URL. 
  # This is how you work with APIs or scrape web data.
# intsalled requests by using :  pip install requests
#We will see get, status_code, headers, text and json methods in requests module:

# get(): to open a network and fetch data from url - it returns a response object
# status_code: After we fetched data, we can check the status of the operation (success, error, etc)
# headers: To check the header types
# text: to extract the text from the fetched response object
# json: to extract json data Let's read a txt file from this website, https://www.w3.org/TR/PNG/iso_8859-1.txt.
print()
# import requests # importing the request module

# url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

# response = requests.get(url) # opening a network and fetching a data
 #print(response) 
 # print(response.status_code) # status code, success:200
# print(response.headers)     # headers information
# print(response.text) # gives all the text from the page