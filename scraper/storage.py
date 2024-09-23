import json
import os
import requests

class StorageStrategy:
    def save(self, data):
        pass

    def save_image(self, url):
        pass

class JSONStorageStrategy(StorageStrategy):
    def __init__(self, output_dir='data', filename='products.json'):
        self.output_dir = output_dir
        self.filename = filename
        self.image_dir = os.path.join(output_dir, 'images')
        os.makedirs(self.image_dir, exist_ok=True)

    def save(self, data):
        with open(os.path.join(self.output_dir, self.filename), 'w') as f:
            json.dump(data, f, indent=4)

    def save_image(self, url):
        image_name = url.split('/')[-1].split('?')[0]
        image_path = os.path.join(self.image_dir, image_name)
        response = requests.get(url)
        with open(image_path, 'wb') as f:
            f.write(response.content)
        return image_path
