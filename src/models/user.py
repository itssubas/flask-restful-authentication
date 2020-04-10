# src/models/user.py
from marshmallow import fields, Schema
import datetime
from . import db
from . import bcrypt

class UserModel(db.Model):
    """
    User Model
    """

    # table name
    __tablename__ = 'users'

    # id = db.Column(db.Integer, primary_key=True)
    # name = db.Column(db.String(128), nullable=False)
    # email = db.Column(db.String(128), unique=True, nullable=False)
    # password = db.Column(db.String(128), nullable=True)
    # created_at = db.Column(db.DateTime)
    # modified_at = db.Column(db.DateTime)

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    deleted_at = db.Column(db.DateTime())

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.fullname = data.get('fullname')
        self.email = data.get('email')
        self.password = self.__generate_hash(data.get('password'))
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            if key == 'password': # add this new line
                self.password = self.__generate_hash(item)
            else:
                setattr(self, key, item)
        self.updated_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        # db.session.delete(self)
        self.deleted_at = datetime.datetime.utcnow()
        db.session.commit()

    @staticmethod
    def get_all_users():
        return UserModel.query.all()

    @staticmethod
    def get_one_user(id):
        return UserModel.query.get(id)

    @staticmethod
    def get_user_by_email(value):
        return UserModel.query.filter_by(email=value).first()


    def __repr(self):
        return '<id {}>'.format(self.id)

    def __generate_hash(self, password):
        return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")

    def check_hash(self, password):
        return bcrypt.check_password_hash(self.password, password.encode('utf-8'))

class UserSchema(Schema):
    """
    User Schema
    """
    id = fields.Int(dump_only=True)
    fullname = fields.Str()
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
