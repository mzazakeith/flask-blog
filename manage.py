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


# Create manager instance 
manager = Manager(app)

# Create migrate instance
migrate = Migrate(app, db)

manager.add_command('server', Server)

manager.add_command('db', MigrateCommand)


