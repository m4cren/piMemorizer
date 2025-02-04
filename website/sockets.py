from .extensions import socketio, emit, send
from flask_socketio import SocketIO, emit, send, join_room, leave_room
from .models import *
from flask_login import current_user

@socketio.on('user-login')
def userLogin(data):
     userID = data['id']

     user = User.query.filter_by(id = userID).first()

     username = user.name

     emit('response-login', {'username': username})

@socketio.on('update-highscore')
def updateHighscore(data):
     highscore = data['score']

     user = User.query.filter_by(id = current_user.id).first()

     if(user.high_score < highscore):
          user.high_score = highscore
          db.session.commit()