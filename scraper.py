from bs4 import BeautifulSoup
import requests;
import time;

def getImages(birds):
    images = []
    for bird in birds:
        page = requests.get(f"https://en.wikipedia.org/wiki/{bird}")
        soup = BeautifulSoup(page.content, 'html.parser')
        images.append(soup.find_all("img"))
        soup.decompose();
    return images;

# write it so if it encounters a repeat it can just reference it
# if url is invalid, find the next

def getImageUrls(birds):
    print('Getting image urls for birds')
    print(birds)
    start = time.time()
    
    urls = []
    images = getImages(birds)

    for index in range(len(images)):
        image = str(images[index][0])
        src_index = image.find("src")
        jpg_index = image.find("jpg/")
        if jpg_index == -1:
            jpg_index = image.find("JPG/")
        final_url = "https://" + image[src_index+7:jpg_index+3].replace("thumb/", "")
        # Accounts for images on the page that come before the main bird image, such as "Good Page"
        if final_url == "https://":
            image = str(images[index][1])
            src_index = image.find("src")
            jpg_index = image.find("jpg/")
            final_url = "https://" + image[src_index+7:jpg_index+3].replace("thumb/", "")
            if final_url == "https://":
                image = str(images[index][2])
                src_index = image.find("src")
                jpg_index = image.find("jpg/")
                final_url = "https://" + image[src_index+7:jpg_index+3].replace("thumb/", "")
                  
        urls.append(final_url)

    print(urls)
    end = time.time()
    print(f"Retrieved {len(birds)} images in {end-start} seconds")
    return urls
