import cloudinary as cloudinary
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from urllib.parse import quote
# from flask_babelex import Babel


app = Flask(__name__,template_folder='template')
app.secret_key ="%^%^$%#$%#$%#$#$%56262626%&^%^&%"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/quanlychuyenbay?charset=utf8mb4' %quote('thudan19')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['CART_KEY'] = 'cart'
cloudinary.config(cloud_name='dexbjwfjg',
                  api_key='575344324738563',
                  api_secret='ibnB7XPQZBtyfTNsvr5KYTVwKzY')


db = SQLAlchemy(app = app)

login = LoginManager(app = app)

# babel = Babel(app=app)
# @babel.localeselector
# def load_locale():
#     return 'vi'