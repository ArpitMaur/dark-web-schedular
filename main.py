from databaseConnection import *
from mainScrapping import *
from datetime import date,datetime,timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from flag import sendLog,sendData
from flag import isNodeBusy
from chechSPA_nonSPA import getfunction
from app import app
import time
# from flask import Flask, jsonify, request
# from flask_cors import CORS
# from flask_socketio import SocketIO

# Flask...

def scrapping():
    print(datetime.now())
    if (isNodeBusy!=True):
        time.sleep(5)
        if collection.count_documents({'isUrgent':True})>0:
                print(f"No of urgent websites :{collection.count_documents({'isUrgent':True})}")
                # sendLog(f"No of urgent websites :{collection.count_documents({'isUrgent':True})}")  #test
                urgent1=collection.find({"isUrgent":True,"status":{"$ne":"running"}},{})
                getfunction(urgent1[0]) 
        else:
            d = datetime.today() - timedelta(hours=0, minutes=30)
            if collection.count_documents({"status":{"$ne":"running"},"time":{"$lte":d}})>0:
                print(f"No of websites whose status not running: {collection.count_documents({'status':{'$ne':'running'},'time':{'$lte':d}})}")
                # sendLog(f"No of websites whose status not running: {collection.count_documents({'status':{'$ne':'running'},'time':{'$lte':d}})}")
                urlList =collection.find({"status":{"$ne":"running"},"time":{"$lte":d}},{})
                getfunction(urlList[0])    
            else:
                print("Every url Scrapped!!") 
                # sendLog("Every url Scrapped!!") 
    else:
        print("Node is Busy!!")        
        # sendLog("Node is Busy!!")        
        


@app.route('/')
def hello_world():
	return 'Hello Darkweb!!'  


scrapping()
sched = BackgroundScheduler(daemon=True)
sched.add_job(scrapping,'interval',minutes=1)
sched.start()

# main flask function
if __name__ == '__main__':
    # socketio.run(app, debug=True)
    app.run()


# Scheduler..
# sched = BackgroundScheduler(daemon=True)
# sched.add_job(scrapping,'interval',minutes=1)
# sched.start()