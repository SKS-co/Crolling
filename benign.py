#################################################
#                                               #
#   File Name: Benign                           #
#                                               #
#   Programmed By: Son                          #
#                                               #
#                                               #
#   Function: Crolling Benign Applications      #
#                  From                         #
#                       APK pure                #
#                                               #
##################### Version ###################
#                                               #
#                                               #
#                                               #
#                                               #
#                                               #
#                                               #
#   V1:                                         #
#                                               #
#                                               #
#                                               #
#################################################
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


#1 앱 페이지로 들어각
#https://apkpure.com/kr/app?page=2, https://apkpure.com/kr/game?page=2

"""

https://apkpure.com/kr/game_action?page=23
https://apkpure.com/kr/art_and_design?page=15
"""

#3/kr/digihud-speedometer/org.mrchops.android.digihud/download?from=details


#카테고리 리스트
categories= {#게임
    "/kr/game_action",
    "/kr/game_adventure",
    "/kr/game_arcade",
    "/kr/game_board",
    "/kr/game_card",
    "/kr/game_casino",
    "/kr/game_casual",
    "/kr/game_educational",
    "/kr/game_music",
    "/kr/game_puzzle",
    "/kr/game_racing",
    "/kr/game_role_playing",
    "/kr/game_simulation",
    "/kr/game_sports",
    "/kr/game_strategy",
    "/kr/game_trivia",
    "/kr/game_word",
    "/kr/game_family",
    "/kr/topic/family",
    "/kr/art_and_design",
    "/kr/auto_and_vehicles",
    "/kr/beauty",
    "/kr/books_and_reference",
    "/kr/business",
    "/kr/comics",
    "/kr/communication",
    "/kr/dating",
    "/kr/education",
    "/kr/entertainment",
    "/kr/events" ,
    "/kr/finance",
    "/kr/food_and_drink",
    "/kr/health_and_fitness",
    "/kr/house_and_home",
    "/kr/libraries_and_demo",
    "/kr/lifestyle",
    "/kr/maps_and_navigation"
    "/kr/medical",
    "/kr/music_and_audio",
    "/kr/news_and_magazines",
    "/kr/parenting",
    "/kr/personalization",
    "/kr/photography",
    "/kr/productivity",
    "/kr/shopping",
    "/kr/social",
    "/kr/sports",
    "/kr/travel_and_local",
    "/kr/video_players",
    "/kr/weather"}


#apkpure url
apkpure = "https://apkpure.com"

#url + categories
url = list()
i = 0
for cat in categories:
    i += 1
    url.append(apkpure + cat) # + "?page=" + 페이지 수

    
print('카테고리 갯수: ', i)

#
for u in url:
    driver = webdriver.Chrome(executable_path='chromedriver')
    #print(url)
    driver.get(url=u)
    print("{0} 다운로드 시작:".format(url))
    #카테고리의 최대 페이지 수
    a_tag = driver.find_elements(By.TAG_NAME, "a")
    for i in a_tag:
        page = i.get_attribute('data-maxpage')
        if page is not None:
            print('max page: ', page)
            page = int(page) +1
            break
    href = list()
    for i in a_tag:
        href.append(i.get_attribute('href'))
    for p in range(1, page):
        if p is 1:
            for i in href:
                if i is not None:
                    if'/download?from=category' in i:
                        print(i)
                        driver.get(url=i)
        else:
            page_url = u+"?page=" + str(p)
            print('current page: ', page_url)
            driver.get(url=page_url)
            #a_tag = driver.find_elements(By.TAG_NAME, "a")
            a_tag = driver.find_elements(By.TAG_NAME, "a")
            href = list()
            for i in a_tag:
                href.append(i.get_attribute('href'))
            for i in href:
                if i is not None:
                    if'/download?from=category' in i:
                        print(i)
                        driver.get(url=i)
            if p % 10 is 0:
                driver.close()
                driver = webdriver.Chrome(executable_path='chromedriver')
