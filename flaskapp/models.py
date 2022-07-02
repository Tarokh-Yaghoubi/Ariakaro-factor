from flaskapp import app
from flask_sqlalchemy import SQLAlchemy
import os 

thedir = os.path.dirname(__file__)
goal_path = os.path.join(thedir, 'aria-data.db')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{0}'.format(goal_path)

db = SQLAlchemy(app)


class AriaKaroFactorial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taxation = db.Column(db.Float, nullable=False)
    taxation_c = db.Column(db.Float, nullable=False)
    value_added = db.Column(db.Float, nullable=False)
    insurance = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'Salary Price {self.taxation}'

        