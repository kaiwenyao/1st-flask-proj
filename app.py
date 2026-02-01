from datetime import datetime
from flask import Flask, jsonify
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
    email: Mapped[str] = mapped_column(db.String(50), nullable=True)


@app.route('/users')
def get_all_users():
    # 1. 构建查询语句： "SELECT * FROM user"
    stmt = db.select(User)

    # 2. 执行并获取结果
    # .scalars() 的作用是把结果行转成 User 对象
    # .all() 获取列表
    users = db.session.execute(stmt).scalars().all()

    # 打印看看
    for user in users:
        print(user.username)

    return "查看控制台日志"

@app.route('/create')
def create():
    user = User(username="admin", password="123")
    db.session.add(user)
    db.session.commit()
    return "数据添加成功"