from databaseConnection import *
from datetime import datetime
from datetime import date
import time

def scrapSuccess(url):
        time.sleep(5)
        collection.update_one({"darkweb_url":url},{'$set':{"isUrgent":False,"status":"done","time":datetime.now(),"failedCount":0}})
        time.sleep(5)
def scrapFailed(url,failedCount):
        time.sleep(5)
        collection.update_one({"darkweb_url":url},{'$set':{"isUrgent":False,"status":"error","time":datetime.now(),"failedCount":failedCount+1}})
        time.sleep(5)
def scrapRunning(url):
        time.sleep(5)
        collection.update_one({"darkweb_url":url},{'$set':{"status":"running","time":datetime.now()}})
        time.sleep(5)

#date-time
today = date.today()
Today_date = today.strftime("%d/%m/%Y")
