from app.models.base import Base, db


class Hospital(Base):
    id = db.Column(db.SmallInteger, nullable=False, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    information = db.Column(db.Text)
    address = db.Column(db.Text)
    phone = db.Column(db.BigInteger)
    email = db.Column(db.Text)


class FirstLevelDepartment(Base):
    id = db.Column(db.SmallInteger, nullable=False, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    phone = db.Column(db.BigInteger)


class SecondLevelDepartment(Base):
    id = db.Column(db.SmallInteger, nullable=False, autoincrement=True, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    phone = db.Column(db.BigInteger)
    first_level_department_id = db.Column(db.SmallInteger,
                                          db.ForeignKey('first_level_department.id'))
    first_level_department = db.relationship('FirstLevelDepartment', backref='second_level_department')
