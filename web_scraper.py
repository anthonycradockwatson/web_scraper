import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import Counter
from PIL import Image
import re
import time

def web_scraper(url, max_images=100):
    def scroll_down(driver): # to account for lazy loading
        time.sleep(2)
        total_height = driver.execute_script("return document.body.scrollHeight")
        step = int(total_height * 0.1)
        current_height = 0

        while current_height < total_height:
            driver.execute_script(f"window.scrollTo(0, {current_height});")
            time.sleep(0.5)
            current_height += step
        
        time.sleep(2)


    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)  
    image_urls=set()
    class_names=[]
    scroll_down(driver)
    img_elements = driver.find_elements(By.TAG_NAME, 'img')
    for img in img_elements:
        class_names.append(img.get_attribute('class'))
    
    counts=Counter(class_names)
    img_class=max(counts, key=counts.get)
    
    images= driver.find_elements(By.XPATH, f"//img[contains(@class, '{img_class}')]")
    
    for img in images:
        if len(image_urls) >= max_images:
            break
        image_urls.add(img.get_attribute('src'))

    driver.quit()
    os.makedirs("assets/images/training", exist_ok=True)
    os.makedirs("assets/images/validation", exist_ok=True)

    regex_pattern=r"(?:image_)(\d+)\.(?:jpg|jpeg|png|img)"
    max_index=0
    for filename in os.listdir("assets/images/validation"):
        match=re.match(regex_pattern, filename)
        if match:
            index=int(match.group(1))
            if index > max_index:
                max_index = index
    
    for x,link in enumerate(image_urls):
        try:
            if x < int(0.8 * len(image_urls)):
                image=requests.get(link).content

                path=os.path.join("assets/images/training", f"image_{max_index+x+1}.jpg")
            else:
                image=requests.get(link).content
                path=os.path.join("assets/images/validation", f"image_{max_index+x+1}.jpg")

            with open(path, 'wb') as f:
                f.write(image)
            
        except Exception as e:
            print("Error Downloading Image:", e)

web_scraper("https://www.pexels.com/search/car%20rears/")