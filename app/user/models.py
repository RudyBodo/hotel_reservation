from app.core.db import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    fullname = db.Column(db.String(50))
    email = db.Column(db.String(20))
    address = db.Column(db.String(50))
    phone_number = db.Column(db.Integer(20))
    password = db.Column(db.String(30))
    role = db.Relationship('Roles', secondary='UserRoles', backref='user',
                                lazy=dynamic)
    profile = db.Relationship('Profile', backref='user',
                                lazy=dynamic)

    def __init__(self, username, fullname, email, address, phone_number, password):
                self.username = username
                self.fullname = fullname
                self.email = email
                self.address = address
                self.phone_number = phone_number
                self.password = password

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Roles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(10))
    description = db.Column(db.String(50))

    def __init__(self, role, description):
        self.role = role
        self.description = description

    def __repr__(Self):
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
        id = db.Column(db.Integer, primary_key=True)
        return '<UserRoles{}>'.format(self.roleid)

class Profile(db.Model):
    __tablename__ = 'profile'
    userid = db.Column(db.Integer, db.ForeignKey(User.id))
    birthdate = db.Column(db.String(50))
    birthplace = db.Column(db.String(50))
    gander = db.Column(db.String(50))

    def __init__(self, userid, birthdate, birthplace, gander):
        self.userid = userid
        self.birthdate = birthdate
        self.birthplace = birthplace
        self.gander = gander

    def __repr__(self):
        return '<Profile{}>'.format(self.userid)
