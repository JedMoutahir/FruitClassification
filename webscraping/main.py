import os
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time

fruits = ['apple', 'banana', 'corn', 'kiwi', 'lemon', 'orange', 'strawberry']

for fruit in fruits:
    folder_name = 'webscraping/fruits/' + fruit.capitalize()
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    count = 0
    start_index = 1
    while count < 250:
        headers = {'User-Agent': UserAgent().random}
        url = f'https://www.google.com/search?q={fruit}+fruit&tbm=isch&ijn={start_index}'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img')
        for i, image in enumerate(images):
            if count >= 250:
                break
            image_url = image['src']
            filename = os.path.join(folder_name, f'{fruit}_{count}.jpg')
            with open(filename, 'wb') as f:
                if 'http' in image_url:
                    f.write(requests.get(image_url, headers=headers).content)
            count += 1
        start_index += 1
        # wait for 10 milliseconds
        time.sleep(0.01)