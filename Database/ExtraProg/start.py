# pip install GoogleImageScraper
# pip install selenium

import os
from GoogleImageScraper import GoogleImageScraper

def GoogleImage():
    oo = open("D:\Project\Gideon\Data.txt",'rt')
    query = str(oo.read())
    oo.close()
    pp = open("D:\Project\Gideon\Data.txt",'r+')
    pp.truncate(0)
    pp.close()
    
    webdriver = "D:\Project\Gideon\Databasewebdriver\chromedriver.exe"
    photos = "D:\Project\Gideon\Database\GooglePhotos"

    search_keys = [f"{query}"]
    number = 10
    head = False
    max = (1000, 1000)
    min = (0,0)

   
    image_search = GoogleImageScraper(webdriver,photos,search_key,number,head,min,max)
    image_urls = image_search.find_image_urls()
    image_search.save_image(image_urls)



    os.startfile(photos)

GoogleImage()