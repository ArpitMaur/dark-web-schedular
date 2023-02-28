# from main import socketio
# from app import socketio
import requests

global isNodeBusy 
isNodeBusy =False
# global socketIO 
# socketIO=None

def sendData(data):
    # socketio.emit('data',data)
    requests.post('http://127.0.0.1/sendData',json={'data':data})

def sendLog(log):
    requests.post('http://127.0.0.1/sendLog',json={'msg':log})
    # socketio.emit('log',log) 