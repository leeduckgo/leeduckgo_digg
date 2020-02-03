# -*- coding:utf-8  -*-

from app import db

class Posts(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    abstract = db.Column(db.String)
    create_time = db.Column(db.DateTime)
    link = db.Column(db.String)
    
    class_name="Posts"
    class_varies=['title','abstract', 'create_time', 'link']
    def get_vary(self, vary_name):
        return eval("self." + vary_name)






