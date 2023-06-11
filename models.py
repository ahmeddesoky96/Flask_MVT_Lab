from flask_sqlalchemy import SQLAlchemy
from flask import url_for
from datetime import datetime


db=SQLAlchemy()


class Post(db.Model):
    __tablename__= 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    body = db.Column(db.String,nullable=False)
    image = db.Column(db.String)
    
    def __str__(self):
        return self.title
    
    @classmethod
    def getAllPost(cls):
        return  cls.query.all()
    
    @classmethod
    def getSpecificPost(cls, id):
        return  cls.query.get_or_404(id)
   
    def deletePost(self):
        db.session.delete(self)
        db.session.commit()
        return True
