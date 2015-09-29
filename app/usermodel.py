__author__ = 'tekvy'
from app import db


class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    gcm_reg_id = db.Column(db.String, nullable=False)

    def __init__(self, name, email, password, gcm_reg_id):
        self.name = name
        self.email = email
        self.password = password
        self.gcm_reg_id = gcm_reg_id

    def to_json(User):
        return {
            "id": User.id,
            "name": User.name,
            "email": User.email,
            "gcm_regid": User.gcm_reg_id}

    def profile_details(User):
        return {
            "id": User.id,
            "name": User.name,
            "email": User.email,
            "gcm_regid": User.gcm_reg_id
            }