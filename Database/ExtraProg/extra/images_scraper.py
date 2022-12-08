#Import libraries
import os
import concurrent.futures
from GoogleImageScraper import GoogleImageScraper

def GoogleImage():
    oo = open("D:\Project\Gideon\Data.txt",'rt')
    query = str(oo.read())
    oo.close()
    pp = open("D:\Project\Gideon\Data.txt",'r+')
    pp.truncate(0)
    pp.close()

def worker_thread(search_key):
    image_scraper = GoogleImageScraper(webdriver_path, image_path, search_key, number_of_images, headless, min_resolution, max_resolution)
    image_urls = image_scraper.find_image_urls()
    image_scraper.save_images(image_urls, keep_filenames)

    #Release resources
    del image_scraper

if __name__ == "__main__":
    #Define file path
    webdriver_path = "D:\Project\Gideon\Databasewebdriver\chromedriver.exe"
    image_path = "D:\Project\Gideon\Database\GooglePhotos"

    #Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
    search_keys = list(set(["cat", "t-shirt"]))

    #Parameters
    number_of_images = 5                # Desired number of images
    headless = False                    # False=  Chrome GUI
    min_resolution = (0, 0)             # Minimum desired image resolution
    max_resolution = (9999, 9999)       # Maximum desired image resolution
    max_missed = 1000                   # Max number of failed images before exit
    number_of_workers = 1               # Number of "workers" used
    keep_filenames = False              # Keep original URL image filenames

    #Run each search_key in a separate thread
    #Automatically waits for all threads to finish
    #Removes duplicate strings from search_keys
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_workers) as executor:
        executor.map(worker_thread, search_keys)

worker_thread('pokemon')