from flask import Flask
from flask_login import LoginManager
from flask_openid import OpenID
from flask_sqlalchemy import SQLAlchemy
import os

from config import basedir

app = Flask(__name__)
app.config.from_object('config') # 引入配置
db = SQLAlchemy(app)


lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app,os.path.join(basedir,'tmp'))
from app import views,models