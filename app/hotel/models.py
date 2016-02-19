from app.core db import db
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
        return '{City}'.format(self.city = city)

class Province(db.Model):
    #set table name
    __tablename__ = 'province'
    id = db.Column(db.integer, primary_key=True)
    province = db.Column(db.String(50))
    code = db.Column(db.String(50))

    def __init__(self, city, code):
        self.province = province
        self.code = code

    def __repr__(self):
        return '{Province}'.format(self.city = city)

class Country(db.Model):
    #set table name
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50))
    code = db.Column(db.String(50))

    def __init__(self, city, code):
        self.country = city
        self.code = code

    def __repr__(self):
        return '{Country}'.format(self.city = city)
        #set table name

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

    def __repr__:
    return '{HotelFacility}'.format(self.hotelid = hotelid)

class Hotel(db.Model):
#set table name
    __tablename__ = 'hotels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(50))
    zipcode = db.Column(db.Integer)
    city_id = db.Column(db.Integer, db.ForeignKey(City.id))
    hotelfacility_id = db.Relationship('HotelFacility',
    city = db.Relationship('city',
            backref=db.backref('hotels', lazy=dynamic))
    province_id = db.column(db.Integer, db.ForeignKey(Province.id))
                        backref='hotels', lazy=dynamic)
    province = db.Relationship('province',
                backref=db.backref('hotels', lazy=dynamic))
    country_id = db.column(db.Integer, db.ForeignKey(Country.id))
    country = db.Relationship('country',
                backref=db.backref('hotels', lazy=dynamic))
    price = db.Column(db.Float)
    reservation_id = db.Column(db.Integer, db.ForeignKey=(Reservation.id))

    def __init__(self, name, address, zipcode,
                city_id, province_id, province, country_id, price, reservation_id):
        self.name = name
        self.address = address
        self.zipcode = zipcode
        self.city_id = city_id
        self.province_id = province_id
        self.country_id = country_id
        self.price = price
        self.reservation_id = reservation_id

    def __repr__(self):
        return {'Hotel'}.format(self.name = name)
