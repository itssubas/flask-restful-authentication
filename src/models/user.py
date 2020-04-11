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
        self.email = self.email + str(datetime.datetime.utcnow().timestamp())
        self.deleted_at = datetime.datetime.utcnow()
        db.session.commit()

    @staticmethod
    def get_all_users():
        users = UserModel.query.filter(UserModel.deleted_at == None).all()
        return users

    @staticmethod
    def get_one_user(id):
        user = UserModel.query.filter(UserModel.deleted_at == None, UserModel.id == id).first()
        return user

    @staticmethod
    def get_user_by_email(value):
        user = UserModel.query.filter(UserModel.deleted_at == None, UserModel.email == value).first()
        return user


    def __repr__(self):
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
