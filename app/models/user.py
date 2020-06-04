from app.models.base import Base, db


class UserIdentity(Base):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.Text)
    user = db.relationship('User', backref='user_identity')


class User(Base):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.Text)
    pwd = db.Column(db.Text)
    email = db.Column(db.Text)
    phone = db.Column(db.BigInteger)
    last_login = db.Column(db.DateTime)
    user_identity_id = db.Column(db.Integer, db.ForeignKey('user_identity.id'))
