# Import flask and template operators
from flask import Flask, render_template
from flask.ext import restful

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy
#Removed migrate until learn how this works
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand


# Define the WSGI application object
app = Flask(__name__)
api = restful.Api(app)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth.controllers import mod_auth as auth_module

# Register blueprint(s)
app.register_blueprint(auth_module)


# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_location.controllers import mod_loc as loc_module

# Register blueprint(s)
app.register_blueprint(loc_module)


# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

class Test(restful.Resource):
    def get(self, name):
        return { 'value': name }

        
api.add_resource(Test, '/post/<string:name>')
