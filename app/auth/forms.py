from flask_wtf import FlaskForm
from wtforms.validators import Required, Email, EqualTo, Length
from wtforms import ValidationError
from wtforms import StringField, PasswordField, BooleanField, SubmitField

from app.models import User
