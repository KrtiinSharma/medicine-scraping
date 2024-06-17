import requests
from bs4 import BeautifulSoup

med_name = "dolo 650"

med_name_new = ""

for i in med_name:
    if (i == " "):
        med_name_new += "%20"
    else:
        med_name_new += i


url = "https://www.netmeds.com/catalogsearch/result/{med_name_new}/all"  # Replace with the actual URL of the website

# Send a GET request to the website and retrieve the HTML content
response = requests.get(url)
html_content = response.content

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find the element containing the product name using appropriate selectors
product_name_element = []
product_name_element = soup.find("span", class_="clsgetname")  # Replace with the appropriate selector for your website

# Extract the product name from the element
# product_name = product_name_element.text.strip()

# Print the extracted product name
print(product_name_element)