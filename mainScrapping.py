from statusHandler import *
from databaseConnection import *
from flag import isNodeBusy
from Spa import *
from  non_spa import *
from flag import sendLog

# Scrapping...
isNodeBusy = False

def getfunction1(darkweb_url,iterator,title_xpath,body_xpath,date_xpath,scrollable,clickable,clickable_btn_xpath,pagination,is_nextbtn,xpath_of_next_btn,xpath_of_pagination_container,tag_name_of_pages,waitTime,failedCount):
        print("Scrapping in progress...")
        # sendLog("Scrapping in progress...")
        isNodeBusy =True
        try:              
                print(darkweb_url,"is Scrapping now...")
                # sendLog(f"{darkweb_url} is Scrapping now...")
                scrapRunning(darkweb_url)
                spa(darkweb_url,iterator,title_xpath,body_xpath,date_xpath,scrollable,clickable,clickable_btn_xpath,pagination,is_nextbtn,xpath_of_next_btn,xpath_of_pagination_container,tag_name_of_pages,waitTime)
                scrapSuccess(darkweb_url)
                print(darkweb_url," Scrapping Done!!")
                # sendLog(f"{darkweb_url} Scrapping Done!!")
                isNodeBusy =False
        except:
                print("not Scrapped!!---->",darkweb_url)
                # sendLog(f"not Scrapped!!----> {darkweb_url}") #test 3
                print("FailedCount is:",str(failedCount+1))
                # sendLog(f"FailedCount is: {str(failedCount+1)}")  #test 2
                scrapFailed(darkweb_url,failedCount) 
                isNodeBusy =False
                

def getfunction2(darkweb_url,iterator,title_xpath,body_xpath,date_xpath,scrollable,clickable,clickable_btn_xpath,pagination,is_nextbtn,xpath_of_next_btn,xpath_of_pagination_container,tag_name_of_pages,waitTime,failedCount):
 
        print("Scrapping in progress...")
        # sendLog("Scrapping in progress...")
        not isNodeBusy 
        try:       
                scrapRunning(darkweb_url)
                Non_spa(darkweb_url,iterator,title_xpath,body_xpath,date_xpath,scrollable,clickable,clickable_btn_xpath,pagination,is_nextbtn,xpath_of_next_btn,xpath_of_pagination_container,tag_name_of_pages,waitTime)
                not isNodeBusy 
                scrapSuccess(darkweb_url)
                print(darkweb_url," Scrapping Done!!")
                # sendLog(f"{darkweb_url} Scrapping Done!!")
                isNodeBusy
        except:
                print("not Scrapped!!---->",darkweb_url )
                # sendLog(f"not Scrapped!!----> {darkweb_url}") 
                print("FailedCount is :",str(failedCount+1))
                # sendLog(f"FailedCount is : {str(failedCount+1)}") 
                scrapFailed(darkweb_url,failedCount)
                isNodeBusy