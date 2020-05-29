"""
@author: Soham Shah
"""

#libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from time import sleep, strftime

#__instaFlayer__v2 (variant-2)
class __instaFlayer__v2():
    
    #init
    def __init__(self, email, password):
        chromedriver_path = 'C://Users//Soham Shah//Desktop//chromedriver.exe'
        self.webdriver = webdriver.Chrome(executable_path = chromedriver_path)
        sleep(2)
        self.email = email
        self.password = password
        self.base_url = 'https://www.instagram.com/'
    
    #sign-in to your account
    def signIn(self):
        self.webdriver.get(self.base_url + 'accounts/login/?source=auth_switcher')
        sleep(3)
        username = self.webdriver.find_element_by_name('username')
        username.send_keys(self.email)
        password = self.webdriver.find_element_by_name('password')
        password.send_keys(self.password)
        button_login = self.webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
        button_login.click()
        sleep(3)
        notnow = self.webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
        notnow.click()
        sleep(3)
        
    def searchHashtag(self, hashtag):
        self.webdriver.get('https://www.instagram.com/explore/tags/' + hashtag)
    
    def searchAccount(self, user):
        self.webdriver.get('https://www.instagram.com/' + user + '/')
        
    #likes %amount of photos 
    def likePhotos(self,amount):
        bot = self.webdriver
       
        bot.find_element_by_class_name('v1Nh3').click()
        i=0
        while i<=amount:
            time.sleep(1)
            bot.find_element_by_class_name('fr66n').click()
            bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            i+=1
    
    #posts random comments on %amount of photos    
    def CommentPhotos(self, amount):
        sleep(2)
        bot = self.webdriver
        options = ['Damnnn Lit', 'On Fire!!!!!!', 'You Look AMAZZZINGGGG', 'Nice Pic!', 'Awesomeness at its height!', 'Cool']
        bot.find_element_by_class_name('v1Nh3').click()
        i=0
        while i<=amount:
            sleep(10)
            try:
                bot.find_element_by_class_name('X7cDz').click()
                comment = bot.find_element_by_class_name('Ypffh')
                comment.send_keys(random.choice(options))
                
                comment.send_keys(Keys.ENTER)
                bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
                i+=1
            except:
                print("No more posts :( ")
                break
    
    #to get the followers of target user
    def get_followers(self, user):
        bot = self.webdriver
        sleep(5)
        bot.get("https://instagram.com/" + user + "/")
        sleep(5)
        bot.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")\
            .click()
        time.sleep(5)
        followers = self._get_names()
        return followers
    
    #follows %amount followers of the user
    def follow(self,lis, amount):
        bot = self.webdriver
        for user in lis[:amount]:
            sleep(6)
            bot.get("https://instagram.com/" + user + "/")
            sleep(10)
            try:
                follow_button = bot.find_element_by_css_selector("#react-root > section > main > div > header > section > div.nZSzR > button")
                if follow_button.text == "Follow":
                    follow_button.click()
            except:
                pass
    
    def _get_names(self):
        bot = self.webdriver
        time.sleep(5)
        scroll_box = bot.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(1) 
            ht = bot.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        bot.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]")\
            .click()
        return names
       
#run __instaFlayer__v2
insta = __instaFlayer__v2('enter-your-username', 'enter-your-password')
insta.signIn()
insta.searchAccount('enter-account-name') # or insta.searchHashtag("enter-hashtag-here")
insta.CommentPhotos(10)
insta.likePhotos(10)
follower_list = insta.get_followers('enter-username')
insta.follow(follower_list, 10)

            
                
            
