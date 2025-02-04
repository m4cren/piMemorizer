from flask import Flask
from .extensions import db, migrate, login_manager, socketio, ip_address
from .sockets import socketio
from os import path
import pymysql

pymysql.install_as_MySQLdb()

def create_website():

     app = Flask(__name__)
     app.config['SECRET_KEY'] = 'secret'
     app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:%40%23OctObEr102704@{ip_address}/test_1?charset=utf8'
     
     db.init_app(app)
     migrate.init_app(app, db)
     socketio.init_app(app)

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

     

     return app

def create_database(app):
    
     with app.app_context():
          db.create_all()
          print("Created Database!")