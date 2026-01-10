import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
url = 'http://books.toscrape.com/'

response = requests.get(url)

if response.status_code == 200:
    data = response.content
    #print(data)
    soup = BeautifulSoup(response.content,'html.parser')
    books = soup.find_all('article',class_="product_pod")
    #print(books[0])
    rows = []
    for book in books:
        title = book.find('h3').find('a')['title']
        price = book.find('p', class_='price_color').get_text()
        link = book.get('href', 'Sin enlace')
        rating_element = book.find('p', class_='star-rating')
        rating = 'Sin rating'
        if rating_element:
            rating_classes = rating_element.get('class', [])
            for cls in rating_classes:
                if cls in ['One', 'Two', 'Three', 'Four', 'Five']:
                    rating = cls
                    break
            rows.append([title,price,link,rating])
        
    headers = ['Titulo','Precio','Link','Rating']
print(tabulate(rows, headers,tablefmt='grid'))