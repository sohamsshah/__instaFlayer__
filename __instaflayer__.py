# -*- coding: utf-8 -*-
"""
Created on Sat May  9 00:13:00 2020

@author: Soham Shah
"""

# import libraries
from instabot import Bot #for posting on instagram
from selenium import webdriver #web-scrapping library
import random
from PIL import Image #imaging library
import requests
from io import BytesIO
from time import sleep, strftime
import json
import urllib3 #url-scrapping
import os

#to get random meme from reddit
def get_meme():
    urllib3.disable_warnings()
    url = 'https://old.reddit.com/r/' + "memes" + '/random.json'
    http = urllib3.PoolManager()
    suffix = ['.jpg','.png','.gif','.bmp']
    while True:
        response = http.request('GET',url)
        thedata = response.data
        parsedjson = json.loads(thedata)
        thefinalurl = parsedjson[0]['data']['children'][0]['data']['url']
        if thefinalurl.endswith('.png') or thefinalurl.endswith('.jpg'):
            response = requests.get(thefinalurl)
            img = Image.open(BytesIO(response.content))
            post_img = image_operations(img)
            post_img.save("#image-path-here")
            print(thefinalurl)
            break
        else:
            print('Not an image')
            
#to get high quality coding image from Unsplash
def get_coding_image():
    res=random.randint(32,108)
    res*=10
    print(res)
    link=f'https://source.unsplash.com/{res}x{res}/?programming,coding'
    response = requests.get(link)
    img = Image.open(BytesIO(response.content))
    img.save('post.jpg')
    print("Image Fetched!")

#getting random cool Cosmos lorem ipsum text from saganipsum.com
def get_random_caption():
    trending_hashtags = "#love #instagood #photooftheday #fashion #beautiful #happy #cute #tbt #like4like #followme #picoftheday #follow #me #selfie #summer #art #instadaily #friends #repost #nature #girl #fun #style #smile #food"
    chromedriver_path = 'your-path-here'
    driver = webdriver.Chrome(executable_path = chromedriver_path)
    driver.get("http://saganipsum.com/")
    caption = driver.find_element_by_id('clip')
    captions = caption.text.split('.')
    print("Caption Fetched !")
    return captions[0] + trending_hashtags

#converting images to best instagram fit size for reddit-memes
def image_operations(img):
    basewidth,hsize = 500,500 
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    rgb_img = img.convert('RGB')
    return rgb_img

#deleting the downloaded image after posting
def del_image():
    file = 'post.jpg.REMOVE_ME' 
    location = "//instagram_automation//Saved" #your-location-path-here 
    path = os.path.join(location, file) 
    os.remove(path) 
    print("%s has been removed successfully" %file)

#posts random memes/coding images from the internet wuth randomly generated caption 
def __instaFlayer__(username, password):
    bot = Bot()
    bot.login(username= username, password= password)
    num = random.choice([0,1])    
    get_meme() if num ==0 else get_coding_image()    
    caption = get_random_caption()
    bot.upload_photo("enter-saved-post-location", caption= caption)
    #logging out, resetting counters and cache and deleting downloaded image
    bot.logout()
    bot.reset_cache()
    bot.reset_counters()
    del_image()

__instaFlayer__("enter-your-username", "enter-your-password")

    
