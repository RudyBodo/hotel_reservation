from app.core.db import db
from models import *
from flask import Blueprint, render_template, request

user_views = Blueprint('user', __name__,
                template_folder='../../templates',
                static_folder='../../static')

@user_views.route('/registration', methods=['POST'], ['GET'])
def reg():
    if request.method =='POST':
        username = reuest.form.get('Username', None)
        fullname = request.form.get('Fullname', None)
        email = request.form.get('Email', None)
        Address = request.form.get('Address', None)
        PhoneNumber = request.form.get('PhoneNumber', None)
        password = request.form.get('Password')
        roles = request.form.get('Roles', None)

@user_views.route('/login', methods=['POST'], ['GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('Username', None)
        password = request.form.get('Password', None)
        return 'login succes'
