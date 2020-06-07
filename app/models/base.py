from app.libs.utils.datetime import datetime_creator
from app.models import db


class Base(db.Model):
    __abstract__ = True
    create_user = db.Column(db.String(20), default='diklios')
    create_time = db.Column(db.DateTime, default=datetime_creator())
    status = db.Column(db.SmallInteger, default=1)
    remark = db.Column(db.String(100))

    def fake_delete(self):
        self.update({'status': '0'})
        db.session.add(self)
        db.session.commit()
