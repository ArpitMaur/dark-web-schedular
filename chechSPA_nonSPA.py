from flask import Flask
from databaseConnection import *
from mainScrapping import getfunction1,getfunction2
from apscheduler.schedulers.background import BackgroundScheduler
from flag import sendData,sendLog

def getfunction(data):
    if data['isSPA']:    
        print("The SPA website: ",data['name']," --> ",data['darkweb_url']," is Scrapping now...")
        # sendLog(data['darkweb_url']+" is Scrapping now...")
        # sendLog("Website name is: "+data["name"])
        getfunction1(data['darkweb_url'],data['iterator'],data['title_xpath'],data['body_xpath'],data['date_xpath'],data['scrollable'],data['clickable'],data['clickable_btn_xpath'],data['pagination'],data['is_nextbtn'],data['xpath_of_next_btn'],data['xpath_of_pagination_container'],data['tag_name_of_pages'],data['waitTime'],data['failedCount']) 
    else:
        print("The Non-SPA Website: ",data["name"]," --> ",data["darkweb_url"]," is Scrapping now...")
        # sendLog(data['darkweb_url']+" is Scrapping now...")
        # sendLog("Website name is: "+data["name"])
        getfunction2(data['darkweb_url'],data['iterator'],data['title_xpath'],data['body_xpath'],data['date_xpath'],data['scrollable'],data['clickable'],data['clickable_btn_xpath'],data['pagination'],data['is_nextbtn'],data['xpath_of_next_btn'],data['xpath_of_pagination_container'],data['tag_name_of_pages'],data['waitTime'],data['failedCount'])













