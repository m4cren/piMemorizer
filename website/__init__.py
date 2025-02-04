import eventlet
eventlet.monkey_patch()
<<<<<<< HEAD
=======

>>>>>>> 79d7d863f63b152934eeb06418f2775033f8b749
from flask import Flask
from .extensions import db, migrate, login_manager, socketio, ip_address
from .sockets import socketio
from os import path
import os
<<<<<<< HEAD
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
=======
>>>>>>> 79d7d863f63b152934eeb06418f2775033f8b749
import pymysql





pymysql.install_as_MySQLdb()

def create_website():

     app = Flask(__name__)
     app.config['SECRET_KEY'] = 'secret_98479186421642961464692146216321'
<<<<<<< HEAD
     app.config['SECRET_KEY'] = 'secret_98479186421642961464692146216321'
     app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
     app.config['SQLALCHEMY_POOL_SIZE'] = 10 
     app.config['SQLALCHEMY_MAX_OVERFLOW'] = 20  
     app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600  
=======
     app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
     app.config['SQLALCHEMY_POOL_SIZE'] = 10  # Number of connections to keep in the pool
     app.config['SQLALCHEMY_MAX_OVERFLOW'] = 20  # Number of connections that can be created above the pool size
     app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600  # How often to recycle connections (in seconds)
    
>>>>>>> 79d7d863f63b152934eeb06418f2775033f8b749
     
     db.init_app(app)
     migrate.init_app(app, db)
     socketio.init_app(app, async_mode='eventlet')
<<<<<<< HEAD

     
=======
>>>>>>> 79d7d863f63b152934eeb06418f2775033f8b749

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
     def shutdown_session(exception=None):
        db.session.remove()

>>>>>>> 79d7d863f63b152934eeb06418f2775033f8b749
     return app

def create_database(app):
    
     with app.app_context():
          db.create_all()
          print("Created Database!")
