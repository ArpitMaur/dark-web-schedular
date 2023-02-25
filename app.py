from flask_cors import CORS
from flask_socketio import SocketIO
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1112#'
socketio = SocketIO(app, cors_allowed_origins="*")
# socketIO=socketio
CORS(app)