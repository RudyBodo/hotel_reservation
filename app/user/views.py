import datetime
from app.core.db import db
from models import *
from app.core.bcrypt import bcrypt
from flask import Blueprint, render_template, request, session, redirect, url_for

user_views = Blueprint('user', __name__,
                        template_folder='../../templates',
                        static_folder='../../static')

@user_views.route("/regist", methods=["POST", "GET"])
def regist():
    #validate form and field
    if request.method == 'POST':
        username = request.form.get('username', None)
        fullname = request.form.get('fullname', None)
        email = request.form.get('email', None)
        address = request.form.get('address', None)
        phone_number = request.form.get('phonenumber', None)
        password = request.form.get('password', None)

        error = []
        if username is None or username == "":
            error.append(dict(field="username",
                              message="input empty"))

        if fullname is None or fullname == "":
            error.append(dict(field="fullname",
                              message="input empty"))

        if email is None or email == "":
            error.append(dict(field="email",
                              message="input empty"))

        if address is None or address == "":
            error.append(dict(field="address",
                              message="input empty"))

        if phone_number is None or phone_number == "":
            error.append(dict(field="phone_number",
                              message="input empty"))

        if password is None or password == "":
            error.append(dict(field="password",
                              message="input empty"))

        if len(error) > 0:
            return render_template("register.html", **locals())

        password = bcrypt.generate_password_hash(password)
        user = User(username, fullname, email,address,phone_number, password)
        user.created_time = datetime.datetime.now()
        #assign role to user
        role = Roles.query.get(2)
        user.user role.append(role)
        db.session.add(user)
        db.session.commit()

        session["user_id"] = user.id
        return redirect(url_for("core.homepage"))

    return render_template("register.html", **locals())

