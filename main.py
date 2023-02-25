# from flask import Flask
from databaseConnection import *
# from mainScrapping import *
from datetime import date,datetime,timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from flag import *
# from flask import Flask, jsonify, request
from chechSPA_nonSPA import getfunction
# from flask_cors import CORS
# from flask_socketio import SocketIO
from app import app, socketio


# Flask...


def scrapping():
    print(datetime.now())
    if (isNodeBusy!=True):
        if collection.count_documents({'isUrgent':True})>0:
                print(f"No of urgent website :{collection.count_documents({'isUrgent':True})}")
                urgent1=collection.find({"isUrgent":True,"status":{"$ne":"running"}},{})
                getfunction(urgent1[0]) 
        else:  
            d = datetime.today() - timedelta(hours=0, minutes=30)
            if collection.count_documents({"status":{"$ne":"running"},"time":{"$lte":d}})>0:
                print(f"No of website whose status not running: {collection.count_documents({'status':{'$ne':'running'},'time':{'$lte':d}})}")
                urlList =collection.find({"status":{"$ne":"running"},"time":{"$lte":d}},{})
                getfunction(urlList[0])    
            else:
                print("Every url Scrapped!!") 
    else:
        print("Node is Busy!!")        
        
   
scrapping()
# Scheduler..
sched = BackgroundScheduler(daemon=True)
sched.add_job(scrapping,'interval',minutes=1)
sched.start()

@app.route('/')
def hello_world():
	return 'Hello Darkweb!!'  



# main flask function
if __name__ == '__main__':
    socketio.run(app, debug=True)
