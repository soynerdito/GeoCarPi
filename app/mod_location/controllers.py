
# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
from flask import request, render_template, flash, \
                 g, session, redirect, url_for

#from app import db
from flask import g, current_app

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_loc = Blueprint('loc', __name__, url_prefix='/loc')

# Set the route and accepted methods


@mod_loc.route('/', methods=['GET', 'POST'])
def index():
    print 'llego'
    return render_template("location/index.html")

