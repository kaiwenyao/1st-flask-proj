from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, false
from sqlalchemy.orm import Mapped, mapped_column
from flask_migrate import Migrate

app = Flask(__name__)

# 配置数据库地址: mysql+驱动://用户名:密码@主机:端口/数据库名
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@localhost:3306/db_learn'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    """用户表"""
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(db.String(50), nullable=False)
    password: Mapped[str] = mapped_column(db.String(200))
    email: Mapped[str] = mapped_column(db.String(50), nullable=False)
