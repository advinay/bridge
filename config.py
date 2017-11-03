import os
import pandas as pd


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

APP_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_DATA_PATH = os.path.join(APP_DIR_PATH, 'static')
