from datetime import timedelta
from flask import Flask
import os
import secrets

secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
app.permanent_session_lifetime = timedelta(days=3)

from flaskapp import views
from flaskapp import models