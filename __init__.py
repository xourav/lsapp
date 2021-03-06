from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:////tmp/test.db'
db=SQLAlchemy(app)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

class User(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(40))
	emailid=db.Column(db.String(40))
	password=db.Column(db.String(40))
	
	def __init__(self,username,emailid,password):
		self.username=username
		self.emailid=emailid
		self.password=password
	def __repr__(self):
		return '<User %r>' % self.username
		
from lsapp import routes
