# from main import socketio

from app import socketio
global isNodeBusy 
isNodeBusy =False
# global socketIO 
# socketIO=None

def sendData(data):
    socketio.emit('data',data)

def sendLog(log):
    socketio.emit('log',log) 