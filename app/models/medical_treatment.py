from app.models.base import Base, db


class Supplier(Base):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    information = db.Column(db.Text)
    address = db.Column(db.Text)
    phone = db.Column(db.BigInteger)
    email = db.Column(db.Text)


class Drugs(Base):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.Text)
    unit = db.Column(db.Text)  # 单位
    price = db.Column(db.Float)
    information = db.Column(db.Text)


class DrugsPurchase(Base):
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    drugs_id = db.Column(db.Integer, db.ForeignKey('drugs.id'))
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    drugs = db.relationship('Drugs', backref='drugs_purchase')
    supplier = db.relationship('Supplier', backref='drugs_purchase')


class Instruments(Base):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.Text)
    price = db.Column(db.Float)
    information = db.Column(db.Text)


class InstrumentsPurchase(Base):
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    instruments_id = db.Column(db.Integer, db.ForeignKey('instruments.id'))
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    drugs = db.relationship('Instruments', backref='instruments_purchase')
    supplier = db.relationship('Supplier', backref='drugs_purchase')


class Projects(Base):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.Text)
    price = db.Column(db.Float)
    information = db.Column(db.Text)


# 挂号
class Register(Base):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    patient_name = db.Column(db.Text)
    gender = db.Column(db.Text)
    phone = db.Column(db.BigInteger)
    first_level_department_id = db.Column(db.SmallInteger, db.ForeignKey('first_level_department.id'))
    first_level_department = db.relationship('FirstLevelDepartment', backref='register')
    second_level_department_id = db.Column(db.SmallInteger, db.ForeignKey('second_level_department.id'))
    second_level_department = db.relationship('SecondLevelDepartment', backref='register')


class Treatment(Base):
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    price = db.Column(db.Float)
    register_id = db.Column(db.Integer, db.ForeignKey('register.id'), primary_key=True)
    drug_id = db.Column(db.Integer, db.ForeignKey('drugs.id'), primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), primary_key=True)
    register = db.relationship('Register', backref='treatment')
    drugs = db.relationship('Drugs', backref='treatment')
    projects = db.relationship('Projects', backref='treatment')
