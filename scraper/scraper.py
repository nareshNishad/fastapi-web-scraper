import requests
from bs4 import BeautifulSoup
import os
import re
from .storage import StorageStrategy
from .notification import NotificationStrategy

def parse_price(price_str):
    price_str = price_str.replace(',', '').replace('₹', '').strip()
    match = re.search(r'[\d.]+', price_str)
    if match:
        return float(match.group())
    return 0.0

class Scraper:
    def __init__(self, storage_strategy: StorageStrategy, notification_strategy: NotificationStrategy):
        self.storage_strategy = storage_strategy
        self.notification_strategy = notification_strategy
        self.products = []

    def scrape(self, limit_pages=None, proxy=None):
        base_url = 'https://dentalstall.com/shop/page/{}/'
        page = 1
        total_scraped = 0
        proxies = {'http': proxy, 'https': proxy} if proxy else None

        while True:
            if limit_pages and page > limit_pages:
                break

            response = requests.get(base_url.format(page), proxies=proxies)
            if response.status_code != 200:
                break

            soup = BeautifulSoup(response.text, 'html.parser')
            product_elements = soup.select('ul.products li.product')

            if not product_elements:
                break

            for product in product_elements:
                # Get the product title
                product_title_element = product.select_one('h2.woo-loop-product__title a')
                # Get the price
                product_price_element = product.select_one('span.price ins span.woocommerce-Price-amount')
                if not product_price_element:
                    # If not on sale, price is directly under span.price
                    product_price_element = product.select_one('span.price span.woocommerce-Price-amount')
                # Get the image URL
                product_image_element = product.select_one('div.mf-product-thumbnail a img')
                if product_title_element and product_price_element and product_image_element:
                    product_title = product_title_element.text.strip()
                    raw_price = product_price_element.text.strip()
                    product_price = parse_price(raw_price)
                    # Get image URL from 'data-lazy-src' or 'src'
                    product_image_url = product_image_element.get('data-lazy-src') or product_image_element.get('src')

                   
                    image_filename = product_image_url.split('/')[-1].split('?')[0]
                    image_path = os.path.join('data', 'images', image_filename)
                    # Download image and save to local storage
                    # os.makedirs(os.path.dirname(image_path), exist_ok=True)
                    # image_response = requests.get(product_image_url, proxies=proxies)
                    # with open(image_path, 'wb') as f:
                    #     f.write(image_response.content)

                    product_data = {
                        'product_title': product_title,
                        'product_price': product_price,
                        'path_to_image': image_path
                    }
                    self.products.append(product_data)
                    total_scraped += 1

            page += 1

        # Save data and notify
        self.storage_strategy.save(self.products)
        self.notification_strategy.notify(f"Scraped {total_scraped} products and updated the database.")
