import os
import requests
from bs4 import BeautifulSoup

fruits = ['apple', 'banana', 'corn', 'kiwi', 'lemon', 'orange', 'strawberry']
prompts = [
    "Ripe", 
    "Unripe", 
    "On a tree", 
    "In a basket", 
    "In a bowl", 
    "Slices", 
    "Close-up", 
    "With leaves", 
    "With stem", 
    "With seeds", 
    "On a plate", 
    "In a smoothie", 
    "In a salad", 
    "In a pie", 
    "In a cocktail", 
    "On a sandwich", 
    "In a dessert", 
    "In a fruit salad", 
    "With other fruits", 
    "In different colors varieties"
]

for fruit in fruits:
    folder_name = 'webscraping/fruits/' + fruit
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for prompt in prompts:
        query = f'{prompt} {fruit}'
        url = f'https://www.google.com/search?q={query}&source=lnms&tbm=isch'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        images = soup.find_all('img')
        for i, image in enumerate(images):
            if i < 20:  # Download only the first 10 images for each query
                image_url = image['src']
                filename = os.path.join(folder_name, f'{query}_{i}.jpg')
                # Download the image is not a gif
                if not image_url.endswith('.gif'):
                    with open(filename, 'wb') as f:
                        f.write(requests.get(image_url).content)
