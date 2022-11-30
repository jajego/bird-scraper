# Grabs from eBird - more reliable and much simpler code 
# with easier to attribute photos, but results in over 2x
# the wait time

from bs4 import BeautifulSoup
import requests;
import time;

def getImages(birds):
    start = time.time()

    images = []
    
    for bird in birds:
        page = requests.get(f"https://ebird.org/species/{bird}")
        soup = BeautifulSoup(page.content, 'html.parser')
        image = soup.img['src']
        images.append(image)
        soup.decompose();
    end = time.time()
    print(f"Retrieved {len(birds)} images in {end-start} seconds")
    return images;
