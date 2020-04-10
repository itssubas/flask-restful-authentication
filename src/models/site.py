# src/models/site.py
from marshmallow import fields, Schema
import datetime
from . import db

class SiteModel(db.Model):
    """
    Site Model
    """

    __tablename__ = 'sites'

    # id = db.Column(db.Integer, primary_key=True)
    # title = db.Column(db.String(128), nullable=False)
    # contents = db.Column(db.Text, nullable=False)
    # created_at = db.Column(db.DateTime)
    # modified_at = db.Column(db.DateTime)


    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255))
    api_id = db.Column(db.String(255))
    api_password = db.Column(db.String(255))
    api_url = db.Column(db.String(255))
    background_color = db.Column(db.String(255))
    redirect_failed = db.Column(db.String(255))
    logo = db.Column(db.String(255)) #TODO: Need to include feature to save file to filesystem
    test_mode = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())
    deleted_at = db.Column(db.DateTime())

    def __init__(self, data):
        self.domain = data.get('domain')
        self.slug = data.get('slug')
        self.api_id = data.get('api_id')
        self.api_password = data.get('api_password')
        self.api_url = data.get('api_url')
        self.background_color = data.get('background_color')
        self.redirect_failed = data.get('redirect_failed')
        self.logo = data.get('logo')
        self.test_mode = data.get('test_mode')
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.updated_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        # db.session.delete(self)
        self.deleted_at = datetime.datetime.utcnow()
        db.session.commit()

    @staticmethod
    # def get_all_blogposts():
    def get_all_sites():
        return SiteModel.query.all()

    @staticmethod
    # def get_one_blogpost(id):
    def get_one_site(id):
        return SiteModel.query.get(id)

    def __repr__(self):
        return '<id {}>'.format(self.id)


class SiteSchema(Schema):
    """
    SiteModel Schema
    """
    id = fields.Int(dump_only=True)
    domain = fields.Str(required=True)
    slug = fields.DateTime(dump_only=True)
    api_id = fields.DateTime(dump_only=True)
    api_password = fields.DateTime(dump_only=True)
    api_url = fields.DateTime(dump_only=True)
    background_color = fields.DateTime(dump_only=True)
    redirect_failed = fields.DateTime(dump_only=True)
    logo = fields.DateTime(dump_only=True)
    test_mode = fields.DateTime(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
