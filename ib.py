from selenium import webdriver

from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(5)
        loginbutton = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        loginbutton.click()
        time.sleep(5)
        user_name_elem = driver.find_element_by_xpath("//input[@name = 'username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name = 'password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(5)

    def like_photo(self,hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(3)
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        # searching for pic link
        hrefs = driver.find_elements_by_tag_name('a')
        print(len(hrefs))
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        #pic_hrefs = [href for href in pic_hrefs if hashtag in href]
        print(hashtag + "Photos: " + str(len(pic_hrefs)))
        print(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_class_name("glyphsSpriteHeart__outline__24__grey_9").click() #glyphsSpriteHeart__outline__24__grey_9
                print("clicked")
                time.sleep(18)
            except Exception as e:
                print(e)
                time.sleep(2)

ig = InstagramBot("arc_arnob", "&&*&*&*&*&**&")
ig.login()
ig.like_photo("instagood")
hashtags = ["skyporn", "street", "newyork", "parisian"]
[ig.like_photo(tag) for tag in hashtags]
