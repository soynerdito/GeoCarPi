
# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,
        default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())


class Location(Base):
    __tablename__ = 'Location'

    latitude = db.Column(Numeric(20, 10), nullable=False)
    longtitude = db.Column(Numeric(20, 10), nullable=False)
    speed = db.Column(Numeric(10, 4), nullable=False)
    elevation = db.Column(Numeric(15, 4), nullable=False)
    timeUTC = db.Column(db.DateTime, timezone=False)

    # New instance instantiation procedure
    def __init__(self):
        pass

    def __repr__(self):
        return '<Location %r>' % (self.latitude)
