import requests
from bs4 import BeautifulSoup


content = requests.get("https://www.bewakoof.com/desi-collection").text
soup = BeautifulSoup(content, 'html.parser')

# For T-shirst title
tshirts = []
for data in soup.find_all('div', {'class': "productCardDetail"}):
    for tshirt in data.find_all('h3'):
        tshirts.append(tshirt.text)

# For Price
price = []
for name in soup.find_all('span', {'class': 'discountedPriceText'}):
    for n in name.find_all('b'):
        price.append(n.text)

# For images
images = []
for div in soup.find_all('div', {'class': 'productCardImg'}):
    for img in div.find_all('img'):
        images.append(img['src'])

# Create csv file
file = open('data.csv', 'w')
file.write('t shirts, prices, images\n')

for i in range(len(images)):
    file.write((f'{tshirts[i]}, {price[i]}, {images[i]}'))
    file.write('\n')

file.close()
