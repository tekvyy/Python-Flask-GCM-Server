from app.usermodel import User
from app import db


def add_user(name, email, password, gcm_regid):
    db.session.add(User(name, email, password, gcm_regid))
    db.session.commit()


def get_users():
    p = User.query.all()
    d1 = {}

    for ujson in p:
        d1.setdefault("users", []).append(User.to_json(ujson))

    return d1


def return_user_details(email):
    profile = User.query.filter_by(email=email).all()

    if profile is not None:
        try:
            b = User.profile_details(profile[0])
            return b

        except IndexError:
            return "error"