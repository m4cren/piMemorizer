from flask import Blueprint, render_template, redirect, url_for
from flask_login import  current_user

actions = Blueprint('actions', __name__)