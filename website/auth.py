from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, current_user, logout_user, login_required, login_remembered
from werkzeug.security import generate_password_hash, check_password_hash
from .models import *
from .views import *

auth = Blueprint('auth', __name__)



@auth.route('/signup', methods = ['POST','GET'])
def signup():

     username = request.form['username']
     password1 = request.form['password1']
     password2 = request.form['password2']

     existing_username = User.query.filter_by(name = username).first()

     if existing_username:
          flash('Username Taken', category='error')
     elif len(username) < 3:
          flash('Username too short', category='error')
     elif password1 != password2:
          flash('Password do not match', category='error')
     else:

          new_user = User(name = username, password = generate_password_hash(password1, method='pbkdf2:sha256'))
          
          db.session.add(new_user)
          db.session.commit()
          login_user(new_user, remember=True)

          return redirect('/homepage')
     
     return redirect('/')

@auth.route('/login/<name>', methods = ['POST','GET'])
def login(name):

     users = User.query.all()
     
     user = User.query.filter_by(name = name).first()
     username = user.name

     if request.method == 'POST':

          password = request.form['password'] 
     
          if check_password_hash(user.password , password):
               login_user(user, remember=True)
               return redirect('/homepage')
          else:
               flash('Wrong Password', category='error')

     return redirect('/')

@auth.route('/logout')
@login_required
def logout():
     logout_user()
     return redirect('/')
