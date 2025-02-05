import eventlet
eventlet.monkey_patch()

<<<<<<< HEAD
=======


>>>>>>> e4a9f2e (New Versione)

from flask import Flask
from .extensions import db, migrate, login_manager, socketio, ip_address
from .sockets import socketio
from os import path
import os


import pymysql





pymysql.install_as_MySQLdb()

def create_website():

     app = Flask(__name__)
     app.config['SECRET_KEY'] = 'secret_98479186421642961464692146216321'
<<<<<<< HEAD
=======
     # app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:%40%23OctObEr102704@{ip_address}/pigame2?charset=utf8'
>>>>>>> e4a9f2e (New Versione)
     app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
     app.config['SQLALCHEMY_POOL_SIZE'] = 10 
     app.config['SQLALCHEMY_MAX_OVERFLOW'] = 20  
     app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600  
<<<<<<< HEAD

=======
   
>>>>>>> e4a9f2e (New Versione)
     
     db.init_app(app)
     migrate.init_app(app, db)
     socketio.init_app(app, async_mode='eventlet')
<<<<<<< HEAD



=======
>>>>>>> e4a9f2e (New Versione)

     from .auth import auth
     from .views import views
     from .actions import actions
     

     app.register_blueprint(views, url_prefix = '/')
     app.register_blueprint(actions, url_prefix = '/')
     app.register_blueprint(auth, url_prefix = '/')

  
     from .models import User

     create_database(app)

     login_manager.login_view = 'views.index'
     login_manager.init_app(app)

     @login_manager.user_loader
     def load_user(id):
          return User.query.get(int(id)) 

<<<<<<< HEAD

=======
>>>>>>> e4a9f2e (New Versione)
     return app

def create_database(app):
    
     with app.app_context():
          db.create_all()
          print("Created Database!")
