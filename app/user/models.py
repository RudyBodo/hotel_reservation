from app.core.db import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    fullname = db.Column(db.String(50))
    email = db.Column(db.String(20))
    address = db.Column(db.String(50))
    phone_number = db.Column(db.Integer)
    password = db.Column(db.String(30))
    profile = db.relationship('Profile', backref='user',
                                lazy = 'dynamic')
    created_time = db.Column(db.DateTime, default = datetime.now)
    lastlogin_time = db.Column(db.DateTime)

    def __init__(self, username, fullname, email, address,
                    phone_number, password, profile, lastlogin_time):
                self.username = username
                self.fullname = fullname
                self.email = email
                self.address = address
                self.phone_number = phone_number
                self.password = password
                self.profile = profile
                self.lastlogin_time = lastlogin_time

    def __repr__(self):
        return '<User{}>'.format(self.username)

class Roles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(15))
    description = db.Column(db.String(50))

    def __init__(self, role, description):
        self.role = role
        self.description = description

    def __repr__(self):
        return '<Roles{}>'.format(self.role)

class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    roleid = db.Column(db.Integer, db.ForeignKey(Roles.id))
    userid = db.Column(db.Integer, db.ForeignKey(User.id))

    def __init__(self, roleid, userid):
        self.roleid = roleid
        self.userid = userid

    def __repr__(self):
        return '<UserRoles{}>'.format(self.roleid)

class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey(User.id))
    birthdate = db.Column(db.DateTime)
    birthplace = db.Column(db.String(50))
    gander = db.Column(db.String(50))

    def __init__(self, userid, birthdate, birthplace, gander):
        self.userid = userid
        self.birthdate = birthdate
        self.birthplace = birthplace
        self.gander = gander

    def __repr__(self):
        return '<Profile{}>'.format(self.userid)