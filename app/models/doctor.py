from app.models.base import Base, db


class Doctor(Base):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.Text)
    gender = db.Column(db.Text)
    height = db.Column(db.Float)
    age = db.Column(db.SmallInteger)
    folk = db.Column(db.Text)
    address = db.Column(db.Text)
    phone = db.Column(db.BigInteger)
    married = db.Column(db.Boolean)
    education = db.Column(db.Text)
    birthday = db.Column(db.Date)
    birthplace = db.Column(db.Text)
    native_place = db.Column(db.Text)
