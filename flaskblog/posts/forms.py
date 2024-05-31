from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


# Form class for User New Post
class PostForm(FlaskForm):
    title      =   StringField('Title', validators=[DataRequired()])
    content    =   TextAreaField('Content', validators=[DataRequired()])

    submit     =   SubmitField('Post')