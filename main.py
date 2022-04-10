from bot import InstaBot
# !pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
from selenium.webdriver.common.by import By
import time


#Follow method and moving to next image
import logging
logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

username, password = "jewelrymdjewelry","kaviglobal123_"

    # Specify which hashtags you want to explore
hashtag_list = ["gold","accessories","earrings","necklace","silver","handmadejewelry",
                    "giftideas","bracelet","ring","etsyshop","diamond","diamonds","bracelets","couture","jewelrydesigner",
                   "jewelryaddict","fashionjewelry","jewelrydesign","jewelryaddict","fashionjewelry","instajewelry",
                   "jewelrygram","gems","gemstone","pendant","gemstones","jewels","jewelry","smallbusiness"]

    #Specify comments
comments_list=["Glowing through <3","Simply Iconic, I'm in love!",
                   "This is amazing! I can't wait to wear it with @jewelrymdjewelry","An absolute example of perfect beauty<3",
                  "This goes so well with @jewelrymdjewelry!",
                   "Same to what @jewelrymdjewelry has, this picture has all the inspiration I needed in my life!",
                  "This is definitely what @jewelrymdjewelry portrays all the time - beauty in simplicity <3",
                  "That is a gorgeous layered look! Many can also be found at @jewelrymdjewelry",
                  "A big mood right here <3",
                   "Just put in an order but I think I need to order all of these to match @jewelrymdjewelry!"]
limits = {}
limits['follow_limit_per_hour'] = randint(5,10)
limits['unfollow_limit_per_hour'] = randint(3,10)
limits['like_limit_per_hour'] = randint(50,80)
limits['comment_limit_per_hour'] = randint(10,19)
            # follow_limit_per_hour = randint(5,10)
            # unfollow_limit_per_hour= randint(3,10)
            # like_limit_per_hour = randint(80,120)
posts_to_reach_per_hashtag = 50


# Iterate through the hashtags stored in "hashtag_list"

new_followed = []
new_unfollowed=[]
my_dict = {}
my_dict_cum = {}

my_dict['followed'] = 0
my_dict['unfollowed']=0
my_dict['likes'] = 0
my_dict['comments'] = 0
my_dict['total_actions'] = 0
my_dict_time = {}
my_dict_time ['like_timer'] =time.time()
my_dict_time ['follow_timer'] =time.time()
my_dict_time ['unfollow_timer']=time.time()
my_dict_time ['comment_timer'] =time.time()
my_dict_cum['followed'] = 0
my_dict_cum['unfollowed']=0
my_dict_cum['likes'] = 0
my_dict_cum['comments'] = 0
my_dict_cum['total_actions'] = 0


if __name__ == "__main__":
    Bot = InstaBot(username,password)
    Bot.login()
    Bot.refresh()
    Bot.num_followers(username)
    Bot.unfollow(username)
    Bot.follow(username)
    Bot.like()
    Bot.comment(num_of_followers)
    Bot.hashtag(hashtag)
    
    
    

