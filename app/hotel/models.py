from app.core.db import db
from app.reservation.models import Reservation

class City(db.Model):
    #set table name
    __tablename__ = 'city'
    id = db.Column(db.integer, primary_key=True)
    city = db.Column(db.String(50))
    code = db.Column(db.String(50))

    def __init__(self, city, code):
        self.city = city
        self.code = code

    def __repr__(self):
        return '<City>{}'.format(self.city)

class Province(db.Model):
    #set table name
    id = db.Column(db.Integer, primary_key=True)
    __tablename__ = 'province'
    province = db.Column(db.String(50))
    code = db.Column(db.String(50))

    def __init__(self, province, code):
        self.province = province
        self.code = code


    def __repr__(self):
        return '<Province>{}'.format(self.province)

class Country(db.Model):
    #set table name
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50))
    code = db.Column(db.String(50))

    def __init__(self, country, code):
        self.country = country
        self.code = code

    def __repr__(self):
        return '<Country>{}'.format(self.country)

class HotelFacility(db.Mdel):
    __tablename__ = 'hotelfacility'
    id = db.column(db.Integer, primary_key=True)
    hotelid = db.Column(db.Integer, db.ForeignKey(Hotel.id))
    garage = db.Column(db.Integer)
    carports = db.Column(db.Integer)
    swimmpingpool = db.Column(db.Integer)

    def __init__(self, hotelid, garage, carports, swimmpingpool):
        self.hotelid = hotelid
        self.garage = garage
        self.carports = carports
        self.swimmingpool = swimmingpool

    def __repr__(self):
        return '<HotelFacility>{}'.format(self.garage)

class Hotel(db.Model):
#set table name
    __tablename__ = 'hotels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    zipcode = db.Column(db.Integer())
    city = db.relationship('City',
            backref='hotels', lazy='dynamic')
    province = db.Relationship('Province',
            backref='hotels', lazy='dynamic')
    country = db.relationship('Country',
            backref='hotels', lazy='dynamic')
    hotelfacility_id = db.relationship('HotelFacility',
            backref='hotels', lazy='dynamic')
    price = db.Column(db.Float())

    def __init__(self, name, address, zipcode,
                 province, price):
        self.name = name
        self.address = address
        self.zipcode = zipcode
        self.city = city
        self.province = province
        self.country = country
        self.price = price

    def __repr__(self):
        return '<Hotel>{}'.format(self.name)
