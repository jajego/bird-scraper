from bs4 import BeautifulSoup
import requests;
import time;
import asyncio

async def getImages(birds):
    start = time.time()
    promises = []
    for bird in birds:
        promises.append(getImage(bird)) # this is an array of promises, not images
    end = time.time()
    print(f"Retrieved {len(birds)} images in {end-start} seconds")
    return await asyncio.gather(*promises)



async def getImage(bird):
    url = f"https://ebird.org/species/{bird}"
    page = await get(url);
    soup = BeautifulSoup(page.content, 'html.parser')
    image = soup.img['src']
    soup.decompose();
    return image


async def get(url):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, requests.get, url)

""""
async def getImages(birds):

    promises = []
    for bird in birds:
        promises.append(getImage(bird))

    return asyncio.gather(promises)

"""""