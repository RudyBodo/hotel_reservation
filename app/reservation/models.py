from app.core.db import db
from datetime impoert datetime

from.app.user.models import User
from app.hotel.models import Hotel
class Reservation(db.Model):
    __tablename__ = 'reservation'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Relationship('user',
                backref='reservation',lazy=dynamic)
    hotelid = db.Relationship('hotels',
                backref='reservation', lazy=dynamic)
    reservationcode = db.Column(db.Integer)
    checkin_date = db.Column(db.DateTime)
    checkout_date = db.Column(db.DateTime)
    room_number = db.Column(db.Integer)
    room = db.Column(db.String(50))
    adult = db.Column(db.Float)
    amount = db.Column(db.Float)
    night = db.Column(db.Float)
    status = db.Column(db.Integer)
    checkin_status = db.Column(db.Integer)
    checkout_status = db.Column(db.Integer)

    def __init__():


    def __repr__():
