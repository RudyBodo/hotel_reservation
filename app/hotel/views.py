from app.core.db import db
from models import *
from flask import Blueprint, request, session, render_template

hotel_views = Blueprint('hotel', __name__,
                template_folder='../../templates',
                static_folder='../../static')


@hotel_views.route('/hotel')
def hotel():
    hotel = Hotel.query.all()
    return render_template('list_hotel.html', **locals())

@hotel_views.route('/hotel/<int:id>')
def viewhotel(id):
    hotel = Hotel.query.get(id)
    return render_template('hotel_details.html', **locals())

@hotel_views.route('/hotel/new', methods=["POST", "GET"])
def newhotel():
    if request.method == 'POST':
        nama_hotel = request.form.get('NamaHotel', None)
        address = request.form.get('Address', None)
        zipcode = request.form.get('Zipcode', None)
        City = request.form.get('City', None)
        Province = request.form.get('Province', None)
        Country = request.form.get('Country', None)
        Price = request.form.get('Price', None)
        added = Hotel(nama_hotel, address, zipcode, city, Province, Country, Price)
        db.session.add(added)
        db.session.commit()

    return render_template('add_hotels.html', **locals())

@hotel_views.route('hotel/del/<int:id')
def delhotel(id):
    hotel = Hotel.query.get(id)
    db.session.delete(hotel)
    db.session.commit()
    return redirect('/hotel')

@hotel.views.route('hotel/clear')
def clearhotel:
    hotel = Hotel.query.all()
    db.session.delete(hotel)
    db.session.commit()
    return redirect('hotel/')
