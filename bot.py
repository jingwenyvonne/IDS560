
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
from selenium.webdriver.common.by import By
import time
import logging


class InstaBot():
    
                    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        
        
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login')
        time.sleep(2)
        user_element = driver.find_element_by_name("username")
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_name("password")
        password_element.send_keys(self.password)
        sleep(4)
        # Click login button
        password_element.send_keys(Keys.RETURN)
        sleep(5)



        # Click "Not Now" on "Save Your Login Info?" popup
        not_now = driver.find_element_by_css_selector("#react-root > section > main > div > div > div > div > button")
        not_now.click()
        sleep(randint(2,5))

        # Click "Not Now" on popup "Turn on Notifications"
        not_now = driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
        not_now.click()
        sleep(randint(2,5))
        
        #refresh
    def refresh(self):
        driver = self.driver
        driver.get("https://www.instagram.com/jewelrymdjewelry/")
        sleep(randint(2,5))
        picture=driver.find_element_by_css_selector("#react-root > section > main > div > div._2z6nI > article > div > div > div > div.v1Nh3.kIKUG._bz0w > a > div > div._9AhH0")
        picture.click()
        sleep(randint(2,5))
        comment = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
        comment.click()
        sleep(randint(2,5))
        comment_hashtags= '#gold,#accessories,#earrings,#necklace'
        comment = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
        comment.send_keys(comment_hashtags)
        sleep(randint(2,5))
        comment_click = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > button > div")
        comment_click.click()
        
        
    #Number of followers function
    def num_followers(self,username):
        driver= self.driver
        url = "https://www.instagram.com/jewelrymdjewelry/"
        sleep(2)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(url)
        sleep(3)
        num_of_followers = driver.find_element_by_css_selector('#react-root > section > main > div > header > section > ul > li:nth-child(2) > a > div > span').text
        if num_of_followers[-1] == 'k':
            num = float(num_of_followers[:-1].replace(',',''))*1000
        elif num_of_followers[-1] == 'm':
            num = float(num_of_followers[:-1].replace(',',''))*1000000
        else:
            num = float(num_of_followers.replace(',',''))
        sleep(2)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return num
      
      


    def unfollow(self,username):
        driver = self.driver
        
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
        if (time.time()-my_dict_time ['unfollow_timer']) < 3600 and my_dict['unfollowed']<limits['unfollow_limit_per_hour']:
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            for i in range(5):
                driver.get("https://www.instagram.com/jewelrymdjewelry/")
                following_=driver.find_element_by_partial_link_text("following")
                following_.click()
                sleep(randint(1,3))
                driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/ul/div/li[1]/div/div[3]/button").click()
                sleep(randint(1,3))
                driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()
                sleep(randint(1,3))
                driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button").click()
                sleep(randint(1,2))
                i+=1
                my_dict['unfollowed']+=1
                my_dict['total_actions']+=1
                my_dict_cum['unfollowed']+=1
                my_dict_cum['total_actions']+=1
                logging.debug('unfollow : {}:total_unfollowed {}: total_actions {}'.format(username, my_dict_cum['unfollowed'],my_dict_cum['total_actions']))
            
        elif (time.time()-my_dict_time ['unfollow_timer']) > 2*3600:
        
            for i in range(5):
                my_dict_time ['unfollow_timer'] =time.time()
                my_dict['unfollowed'] = 0
                limits['unfollow_limit_per_hour']= randint(3,10)
                driver.get("https://www.instagram.com/jewelrymdjewelry/")
                following_=driver.find_element_by_partial_link_text("following")
                following_.click()
                sleep(randint(1,5))
                driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/ul/div/li[1]/div/div[3]/button").click()
                sleep(randint(1,5))
                driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()
                sleep(randint(1,5))
                driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button").click()
                sleep(randint(1,5))
                # Increment "unfollowed" counter, add username to new_unfollowed list
                new_unfollowed.append(username)
                i+=1
                my_dict['unfollowed'] += 1
                my_dict['total_actions'] +=1
                my_dict_cum['unfollowed']+=1
                my_dict_cum['total_actions']+=1
                logging.debug('unfollow : {}:total_unfollowed {}: total_actions {}'.format(username, my_dict_cum['unfollowed'],my_dict_cum['total_actions']))
           
        elif (time.time()-my_dict_time ['unfollow_timer']) > 3600 and my_dict['unfollowed']<limits['unfollow_limit_per_hour']:
            
            for i in range(5):
                my_dict_time ['unfollow_timer'] =time.time()
                my_dict['unfollowed'] = 0
                limits['unfollow_limit_per_hour']= randint(3,10)
                driver.get("https://www.instagram.com/jewelrymdjewelry/")
                following_=driver.find_element_by_partial_link_text("following")
                following_.click()
                sleep(randint(1,5))
                driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/ul/div/li[1]/div/div[3]/button").click()
                sleep(randint(1,5))
                driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()
                sleep(randint(1,5))
                driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[1]/div/div[3]/div/button").click()
                sleep(randint(1,5))
                # Increment "unfollowed" counter, add username to new_unfollowed list
                new_unfollowed.append(username)
                i+=1
                my_dict['unfollowed'] += 1
                my_dict['total_actions'] +=1
                my_dict_cum['unfollowed']+=1
                my_dict_cum['total_actions']+=1
                logging.debug('unfollow : {}:total_unfollowed {}: total_actions {}'.format(username, my_dict_cum['unfollowed'],my_dict_cum['total_actions']))
            

   

    def follow(self,username):

        driver = self.driver
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
        follow_ = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.UE9AK > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button > div")
        username = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.UE9AK > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.e1e1d > div > span > a").text

        if (time.time()-my_dict_time ['follow_timer']) < 3600 and my_dict['followed']<limits['follow_limit_per_hour']:
            # Click follow
            follow_.click()
            sleep(randint(30,60))
            # Increment "followed" counter, add username to new_followed list
            new_followed.append(username)
            my_dict['followed'] += 1
            my_dict['total_actions'] +=1
            my_dict_cum['followed'] += 1
            my_dict_cum['total_actions'] +=1
            logging.debug('follow : {}:total_followed {}: total_actions {}'.format(username, my_dict_cum['followed'],my_dict_cum['total_actions']))

        elif (time.time()-my_dict_time ['follow_timer']) > 2*3600:
            my_dict_time ['follow_timer'] =time.time()
            my_dict['followed'] = 0
            limits['follow_limit_per_hour'] = randint(5,10)
            # Click follow
            follow_.click()
            sleep(randint(30,60))
            # Increment "followed" counter, add username to new_followed list
            new_followed.append(username)
            my_dict['followed'] += 1
            my_dict['total_actions'] +=1
            my_dict_cum['followed'] += 1
            my_dict_cum['total_actions'] +=1
            logging.debug('follow : {}:total_followed {}: total_actions {}'.format(username, my_dict_cum['followed'],my_dict_cum['total_actions']))

        elif (time.time()-my_dict_time ['follow_timer']) > 3600 and my_dict['followed']<limits['follow_limit_per_hour']:
            my_dict_time ['follow_timer'] =time.time()
            my_dict['followed'] = 0
            limits['follow_limit_per_hour'] = randint(5,10)
            # Click follow
            follow_.click()
            sleep(randint(30,60))
            # Increment "followed" counter, add username to new_followed list
            new_followed.append(username)
            my_dict['followed'] += 1
            my_dict['total_actions'] +=1
            my_dict_cum['followed'] += 1
            my_dict_cum['total_actions'] +=1
            logging.debug('follow : {}:total_followed {}: total_actions {}'.format(username, my_dict_cum['followed'],my_dict_cum['total_actions']))


    #like function
    def like (self):

        driver= self.driver
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
        if (time.time()-my_dict_time ['like_timer']) < 3600 and my_dict['likes'] <limits['like_limit_per_hour']:
            like = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button")
            like.click()
            sleep(randint(30,60))
            # Increment "likes" counter
            my_dict['likes'] += 1
            my_dict['total_actions'] +=1
            my_dict_cum['likes'] += 1
            my_dict_cum['total_actions'] +=1
            logging.debug('like: total_likes {}: total_actions {}'.format( my_dict_cum['likes'],my_dict_cum['total_actions']))

        elif (time.time()-my_dict_time ['like_timer']) > 2*3600:
            my_dict_time ['like_timer'] = time.time()
            my_dict['likes'] = 0
            limits['like_limit_per_hour'] = randint(80,120)
            like = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button")
            like.click()
            sleep(randint(30,60))
            # Increment "likes" counter
            my_dict['likes'] += 1
            my_dict['total_actions'] +=1
            my_dict_cum['likes'] += 1
            my_dict_cum['total_actions'] +=1
            logging.debug('like: total_likes {}: total_actions {}'.format( my_dict_cum['likes'],my_dict_cum['total_actions']))

        elif (time.time()-my_dict_time ['like_timer']) > 3600 and my_dict['likes'] <limits['like_limit_per_hour']:
            my_dict_time ['like_timer'] = time.time()
            my_dict['likes'] = 0
            limits['like_limit_per_hour'] = randint(80,120)
            like = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button")
            like.click()
            sleep(randint(30,60))
            # Increment "likes" counter
            my_dict['likes'] += 1
            my_dict['total_actions'] +=1
            my_dict_cum['likes'] += 1
            my_dict_cum['total_actions'] +=1
            logging.debug('like: total_likes {}: total_actions {}'.format( my_dict_cum['likes'],my_dict_cum['total_actions']))


    #Comment function
    def comment(self, num_of_followers):

        driver= self.driver
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
        if (time.time()-my_dict_time ['comment_timer']) < 3600 and my_dict['comments'] <limits ['comment_limit_per_hour']:
            comment = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
            comment.click()
            sleep(randint(1,5))
            # Use "randint" to post different comments
            rand_comment = randint(1,len(comments_list))
            if num_of_followers>20000:
                pick_comment = 'If you are interested being a brand ambassador please leave us a message on our page'
            else:
                pick_comment=comments_list[rand_comment]
            comment = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
            comment.send_keys(pick_comment)
            sleep(randint(1,5))
            comment_click = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > button > div")
            comment_click.click()
            sleep(randint(30,60))
            # Increment "comments" counter
            my_dict['comments'] += 1
            my_dict['total_actions'] +=1
            my_dict_cum['comments'] += 1
            my_dict_cum['total_actions'] +=1
            logging.debug('comment:total_comments {}: total_actions {}'.format( my_dict_cum['comments'],my_dict_cum['total_actions']))

        elif (time.time()-my_dict_time ['comment_timer']) > 2*3600:
            my_dict['comments'] = 0
            my_dict_time ['comment_timer'] =time.time()
            limits ['comment_limit_per_hour'] = randint(30,50)
            comment = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
            comment.click()
            sleep(randint(1,5))
            # Use "randint" to post different comments
            rand_comment = randint(1,len(comments_list))
            #rand_comment=random.randrange(0,5)
            if num_of_followers>20000:
                pick_comment = 'If you are interested being a brand ambassador please leave us a message on our page'
            else:
                pick_comment=comments_list[rand_comment]
            comment = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
            comment.send_keys(pick_comment)
            sleep(randint(2,4))
            comment_click = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > button > div")
            comment_click.click()
            sleep(randint(30,60))
            # Increment "comments" counter
            my_dict['comments'] += 1
            my_dict['total_actions'] +=1
            my_dict_cum['comments'] += 1
            my_dict_cum['total_actions'] +=1
            logging.debug('comment:total_comments {}: total_actions {}'.format( my_dict_cum['comments'],my_dict_cum['total_actions']))

        elif (time.time()-my_dict_time ['comment_timer']) > 3600 and my_dict['comments'] < limits ['comment_limit_per_hour']:
            my_dict['comments'] = 0
            my_dict_time ['comment_timer'] =time.time()
            limits ['comment_limit_per_hour'] = randint(30,50)
            comment = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
            comment.click()
            sleep(randint(1,5))
            # Use "randint" to post different comments
            rand_comment = randint(1,len(comments_list))
            #rand_comment=random.randrange(0,5)
            if num_of_followers>20000:
                pick_comment = 'If you are interested being a brand ambassador please leave us a message on our page'
            else:
                pick_comment=comments_list[rand_comment]
            comment = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
            comment.send_keys(pick_comment)
            sleep(randint(1,5))
            comment_click = webdriver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > button > div")
            comment_click.click()
            sleep(randint(30,60))
            # Increment "comments" counter
            my_dict['comments'] += 1
            my_dict['total_actions'] +=1
            my_dict_cum['comments'] += 1
            my_dict_cum['total_actions'] +=1
            logging.debug('comment:total_comments {}: total_actions {}'.format( my_dict_cum['comments'],my_dict_cum['total_actions']))

    def hashtag(self, hashtag):
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

        for hashtag in hashtag_list:
            driver= self.driver
            # Navigate to Instagram "explore/tags" page for current hashtag
            driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
            sleep(randint(1,2))

            # Click on the second thumbnail in the current hashtag's explore page
            first_thumbnail = driver.find_element_by_css_selector("#react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(2) > a > div > div._9AhH0")
            first_thumbnail.click()
            sleep(randint(1,2))

            try:
                # Iterate through the current hashtag
                for _ in range(posts_to_reach_per_hashtag):
                    try:
                        follow_ = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.UE9AK > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button > div")
                        username = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.UE9AK > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.e1e1d > div > span > a").text
                        number_of_followers  = num_followers(username)
                        sleep(randint(1,3))

                        if my_dict['total_actions']>=349 and my_dict['total_actions']<350:
                            unfollow()
                        elif my_dict['total_actions']>=350:
                            print('Actions during this session')
                            my_dict.items()
                            print('Total actions')
                            my_dict_cum.items()
                            refresh()
                            sleep(86400)
                            my_dict['followed'] = 0
                            my_dict['unfollowed']=0
                            my_dict['likes'] = 0
                            my_dict['comments'] = 0
                            my_dict['total_actions'] = 0
                            my_dict_time ['like_timer'] =time.time()
                            my_dict_time ['follow_timer'] =time.time()
                            my_dict_time ['unfollow_timer']=time.time()
                            my_dict_time ['comment_timer'] =time.time()
                        elif follow_.text == "Follow" and username != "jewelrymdjewelry" and number_of_followers >= 100:

                            follow()
                            sleep(randint(1,3))
                            like()
                            sleep(randint(1,3))
                            comment(number_of_followers)
                            sleep(randint(1,3))
        #                Click "next" to go to next picture within the same hashtag
                        next = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.Z2Inc._7c9RR > div > div.l8mY4.feth3 > button")
                        next.click()
                        sleep(randint(2,5))
                    except Exception as ex:
                        # Write out what type of Exception
                        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                        message = template.format(type(ex).__name__, ex.args)
                        print(message)
                        driver_len = len(driver.window_handles) #fetching the Number of Opened tabs
                        if driver_len > 1: # Will execute if more than 1 tabs found.
                            for i in range(driver_len - 1, 0, -1):
                                driver.switch_to.window(driver.window_handles[i]) #will close the last tab first.
                                driver.close()
                            driver.switch_to.window(driver.window_handles[0]) # Switching the driver focus to First tab.
        #               Click "next" to go to next picture within the same hashtag
                        next = driver.find_element_by_css_selector("body > div.RnEpo._Yhr4 > div.Z2Inc._7c9RR > div > div.l8mY4.feth3 > button")
                        next.click()
                        sleep(randint(2,5))



            except Exception as ex:

                # Write out what type of Exception
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                driver_len = len(driver.window_handles) #fetching the Number of Opened tabs
                if driver_len > 1: # Will execute if more than 1 tabs found.
                    for i in range(driver_len - 1, 0, -1):
                        driver.switch_to.window(driver.window_handles[i]) #will close the last tab first.
                        driver.close()
                    driver.switch_to.window(driver.window_handles[0]) # Switching the driver focus to First tab.
                print(message)



        my_dict_cum.items()



        
