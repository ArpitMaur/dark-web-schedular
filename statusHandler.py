from databaseConnection import *
from datetime import datetime
from datetime import date

from pymongo import MongoClient

def scrapSuccess(url):
        collection.update_one({"darkweb_url":url},{'$set':{"isUrgent":False,"status":"done","time":datetime.now(),"failedCount":0}})
def scrapFailed(url,failedCount):
        collection.update_one({"darkweb_url":url},{'$set':{"isUrgent":False,"status":"error","time":datetime.now(),"failedCount":failedCount+1}})
def scrapRunning(url):
    collection.update_one({"darkweb_url":url},{'$set':{"status":"running","time":datetime.now()}})


#date-time
today = date.today()
Today_date = today.strftime("%d/%m/%Y")
