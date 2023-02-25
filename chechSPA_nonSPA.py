from flask import Flask
from databaseConnection import *
from mainScrapping import getfunction1,getfunction2
from datetime import date,datetime,timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from flag import *

def getfunction(data):
    if data['isSPA']:    
        print(f"No of urgent website :{collection.count_documents({'isUrgent':True})}")
        print(data["darkweb_url"])
        getfunction1(data["darkweb_url"],data["iterator"],data["title_xpath"],data["body_xpath"],data["date_xpath"],data["scrollable"],data["clickable"],data["clickable_btn_xpath"],data["pagination"],data["is_nextbtn"],data["xpath_of_next_btn"],data["xpath_of_pagination_container"],data["tag_name_of_pages"],data["waitTime"],data["failedCount"]) 
    else:
        print(f"No of urgent website :{collection.count_documents({'isUrgent':True})}")
        print(data["darkweb_url"])
        getfunction2(data["darkweb_url"],data["iterator"],data["title_xpath"],data["body_xpath"],data["date_xpath"],data["scrollable"],data["clickable"],data["clickable_btn_xpath"],data["pagination"],data["is_nextbtn"],data["xpath_of_next_btn"],data["xpath_of_pagination_container"],data["tag_name_of_pages"],data["waitTime"],data["failedCount"])
















    #     else:
    #         if(collection.count_documents({'isUrgent':True})==0):
    #             d = datetime.today() - timedelta(hours=0, minutes=30)
    #             if items['isSPA']:
    #                 if collection.count_documents({"status":{"$ne":"running"},"time":{"$lte":d}})>0:
    #                     print(f"No of website whose status not running: {collection.count_documents({'status':{'$ne':'running'},'time':{'$lte':d}})}")
    #                     urlList =collection.find({"status":{"$ne":"running"},"time":{"$lte":d}},{})
    #                     print(urlList[0]["darkweb_url"])            
    #                     getfunction1(urlList[0]["darkweb_url"],urlList[0]["iterator"],urlList[0]["title_xpath"],urlList[0]["body_xpath"],urlList[0]["date_xpath"],urlList[0]["scrollable"],urlList[0]["clickable"],urlList[0]["clickable_btn_xpath"],urlList[0]["pagination"],urlList[0]["is_nextbtn"],urlList[0]["xpath_of_next_btn"],urlList[0]["xpath_of_pagination_container"],urlList[0]["tag_name_of_pages"],urlList[0]["waitTime"],urgent1[0]["failedCount"])  
    #             else:
    #                 if collection.count_documents({"status":{"$ne":"running"},"time":{"$lte":d}})>0:
    #                     print(f"No of website whose status not running: {collection.count_documents({'status':{'$ne':'running'},'time':{'$lte':d}})}")
    #                     urlList =collection.find({"status":{"$ne":"running"},"time":{"$lte":d}},{})
    #                     print(urlList[0]["darkweb_url"]) 
    #                     getfunction2(urlList[0]["darkweb_url"],urlList[0]["iterator"],urlList[0]["title_xpath"],urlList[0]["body_xpath"],urlList[0]["date_xpath"],urlList[0]["scrollable"],urlList[0]["clickable"],urlList[0]["clickable_btn_xpath"],urlList[0]["pagination"],urlList[0]["is_nextbtn"],urlList[0]["xpath_of_next_btn"],urlList[0]["xpath_of_pagination_container"],urlList[0]["tag_name_of_pages"],urlList[0]["waitTime"],urgent1[0]["failedCount"])  
    # else:                    
    #     print("Node is Busy!!")   
