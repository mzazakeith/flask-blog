# Import db from app factory
from app import create_app, db
from flask_script import Manager, Server

# Connect to models
from app.models import User, Post
# Set up migrations
from flask_migrate import Migrate, MigrateCommand

# Creating app instance
# app = create_app('test')
app = create_app('development')
# app = create_app('production')

