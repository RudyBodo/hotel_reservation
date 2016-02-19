from app.core.db import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    fullname = db.Column(db.String(50))
    email = db.Column(db.String(20))
    address = db.Column(db.String(50))
    phone_number = db.Column(db.Integer)
    password = db.Column(db.String(30))
    userrole = db.Column(db.Integer, db.ForeignKey=(UserRoles.id))

    def __init__(self, username, fullname, email,
                    address, phone_number, password):
                self.username = username
                self.fullname = fullname
                self.email = email
                self.address = address
                self.phone_number = phone_number
                self.password = password

    def __repr__(self):
        return {'User'}.format(self.username = username)

class Roles(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(10))
    description = db.Column(db.String(50))
    userroles = db.Column(db.Integer, db.ForeignKey(UserRoles.id))

    def __init__(self, role, description):
        self.role = role
        self.description = description

    def __repr__(Self):
        return {'Roles'}.format(self.role = role)

class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer, primary_key=True)
    roleid = db.Relationship('roles',
                backref='user_roles', lazy=dynamic)
    userid = db.Relationship('user',
                backref='user_roles', lazy=dynamic)

    def __init__(self, roleid, userid):
        self.roleid = roleid
        self.userid = userid

    def __repr__(self):
        return {'UserRoles'}.format(self.roleid = roleid)
