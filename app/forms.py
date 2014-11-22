from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class DecisionForm(Form):
    title = StringField('title', validators=[DataRequired()])

class ChoicesForm(Form):
    title = StringField('title', validators=[DataRequired()])
