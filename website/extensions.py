from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO, emit, send
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
socketio = SocketIO()
login_manager = LoginManager()

ip_address = '192.168.1.20'