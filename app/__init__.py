from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail

from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# Instances of flask extensions
# Instance of LoginManger and using its methods
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
