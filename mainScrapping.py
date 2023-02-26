from statusHandler import *
from databaseConnection import *
from flag import *
from Spa import spa
from  non_spa import Non_spa
from flag import sendData,sendLog


# Scrapping...
# global isNodeBusy
isNodeBusy = False

def getfunction1(darkweb_url,iterator,title_xpath,body_xpath,date_xpath,scrollable,clickable,clickable_btn_xpath,pagination,is_nextbtn,xpath_of_next_btn,xpath_of_pagination_container,tag_name_of_pages,waitTime,failedCount):
        print("Scrapping in progress...")
        sendLog("Scrapping in progress...")
        isNodeBusy =True
        try:              
                print(darkweb_url,"is Scrapping now...")
                scrapRunning(darkweb_url)
                spa(darkweb_url,iterator,title_xpath,body_xpath,date_xpath,scrollable,clickable,clickable_btn_xpath,pagination,is_nextbtn,xpath_of_next_btn,xpath_of_pagination_container,tag_name_of_pages,waitTime)
                scrapSuccess(darkweb_url)
                print(darkweb_url," Scrapping Done!!")
                sendLog(darkweb_url," Scrapping Done!!")
                isNodeBusy =False
        except:
                print("Scrapping failed!!...Website not Scrapped!!---->",darkweb_url)
                sendLog("Scrapping failed!!...Website not Scrapped!!---->",darkweb_url)
                print("FailedCount is:",failedCount+1)
                sendLog("FailedCount is:",failedCount+1)
                scrapFailed(darkweb_url,failedCount)
                isNodeBusy =False
                

def getfunction2(darkweb_url,iterator,title_xpath,body_xpath,date_xpath,scrollable,clickable,clickable_btn_xpath,pagination,is_nextbtn,xpath_of_next_btn,xpath_of_pagination_container,tag_name_of_pages,waitTime,failedCount):
 
        print("Scrapping in progress...")
        not isNodeBusy 
        try:              
                print(darkweb_url," is Scrapping now...This is Non-SPA website")
                sendLog(darkweb_url," is Scrapping now...This is Non-SPA website")
                scrapRunning(darkweb_url)
                Non_spa(darkweb_url,iterator,title_xpath,body_xpath,date_xpath,scrollable,clickable,clickable_btn_xpath,pagination,is_nextbtn,xpath_of_next_btn,xpath_of_pagination_container,tag_name_of_pages,waitTime)
                not isNodeBusy 
                scrapSuccess(darkweb_url)
                print(darkweb_url," Scrapping Done!!")
                sendLog(darkweb_url," Scrapping Done!!")
                isNodeBusy
        except:
                print("not Scrapped!!---->",darkweb_url ," Scrapping Failed")
                sendLog("not Scrapped!!---->",darkweb_url ," Scrapping Failed")
                print("FailedCount is :",failedCount+1)
                sendLog("FailedCount is :",failedCount+1)
                scrapFailed(darkweb_url,failedCount)
                isNodeBusy