from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    mobile_num = db.Column(db.Integer(), unique=True, nullable=False)
    email_id = db.Column(db.String(50), unique=True, nullable=False)
    gender = db.Column(db.String(10), unique=True, nullable=False)
    d_o_b = db.Column(db.String(15))
    qualification = db.Column(db.String(50))
    techStacks = db.Column(db.String(80))
    img = db.Column(db.Text, unique=True, nullable=False)
    desc = db.Column(db.String(500))

