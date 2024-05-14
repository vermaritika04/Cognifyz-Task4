import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.flipkart.com/search?q=phones+under+20%2C000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the class names for product name, price, and rating
product_name_class = 'KzDlHZ'
price_class = 'Nx9bqj _4b5DiR'

# Create a CSV file to store the data
with open('flipkart_products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Product Name', 'Price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Find the product name and price for each phone listing
    product_listings = soup.find_all('div', class_='yKfJKb row')
    for listing in product_listings:
        product_name = listing.find('div', class_=product_name_class).text
        price = listing.find('div', class_=price_class).text

        # Write the data to the CSV file
        writer.writerow({'Product Name': product_name, 'Price': price})

print("Data has been saved to flipkart_products.csv")
