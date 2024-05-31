from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin


# Decorator function to reload the User from user_id store in the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Model Class for User table
class User(db.Model, UserMixin):

    # Column for User table
    id          =  db.Column(db.Integer, unique = True, primary_key=True)
    username    =  db.Column(db.String(20), unique = True, nullable = False)
    email       =  db.Column(db.String(120), unique = True, nullable = False)
    image_file  =  db.Column(db.String(20), nullable= False, default='default.jpg')
    password    =  db.Column(db.String(60), nullable = False)

    # Relationship between User and Post
    posts = db.relationship('Post', backref = 'author', lazy = True)


    # Password reset method
    def get_reset_token(self, expires_sec=1800):
        expires_sec = int(expires_sec)
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)  # Ensure correct secret key
        return s.dumps({'user_id': self.id}).decode('utf-8')

    # Verify reset token method
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])  # Corrected Serializer usage
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    # Representation method for User Class
    def __repr__(self):
            return f"User('{self.username}', '{self.email}', '{self.image_file}')"
    


# Model class for Post table
class Post(db.Model):

    # Columns for the Post table
    id           =  db.Column(db.Integer, primary_key = True)
    title        =  db.Column(db.String(100), nullable = False)
    date_posted  =  db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content      =  db.Column(db.Text, nullable = False) 

    # Foreign key for establishing Relationship with User table
    user_id  =  db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    # Representation method for Post class
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"