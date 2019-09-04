"""
程序工厂函数, 延迟创建程序实例
"""
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()


def create_app(config_name='development'):
    """
    默认创建开发环境的app对象
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)

    # 附加路由和自定义的错误页面
    from app.auth import auth as auth_bp
    app.register_blueprint(auth_bp)  # 注册蓝本
    from app.todo import todo as todo_bp
    app.register_blueprint(todo_bp, url_prefix='/todo')  # 注册蓝本

    return app
