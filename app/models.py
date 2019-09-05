from flask_login import UserMixin
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from . import  login_manager


class Role(db.Model):
    """用户类型"""
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role % r>' % self.name


"""
Flask-Login 提供了一个 UserMixin 类,包含常用方法的默认实现,且能满足大多数需求。
    1). is_authenticated    用户是否已经登录?
    2). is_active           是否允许用户登录?False代表用户禁用
    3). is_anonymous        是否匿名用户?
    4). get_id()            返回用户的唯一标识符
"""


class User(UserMixin, db.Model):
    """用户"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # 电子邮件地址email,相对于用户名而言,用户更不容易忘记自己的电子邮件地址。
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))  # 加密的密码
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        # generate_password_hash(password, method= pbkdf2:sha1 , salt_length=8) :密码加密的散列值。
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        # check_password_hash(hash, password) :密码散列值和用户输入的密码是否匹配.
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return '<User % r>' % self.username

# 加载用户的回调函数;如果能找到用户,返回用户对象;否则返回 None 。
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
