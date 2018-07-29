from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.update({
    # 'SQLALCHEMY_DATABASE_URI': Config.SQLALCHEMY_DATABASE_URI,
    'SECRET_KEY': 'super-secret',
    'FLASK_ENV': Config.FLASK_ENV
})

import lift_api.views
