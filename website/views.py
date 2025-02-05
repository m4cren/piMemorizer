from flask import Blueprint, render_template, redirect, url_for
from flask_login import  current_user,  login_required, login_remembered
from .models import User

views = Blueprint('views', __name__)




@views.route('/')
def index():

     users = User.query.order_by(User.high_score.desc(), User.speed_score.desc()).all()
     return render_template('index.html', users = users)

@views.route('/homepage')
@login_required
def homepage():
     users = User.query.order_by(User.high_score.desc(), User.speed_score.desc()).all()
  
     return render_template('homepage.html', users = users)