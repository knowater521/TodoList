from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError

from app.models import User


class LoginForm(FlaskForm):
    """用户登录表单"""
    email = StringField('电子邮箱', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    email = StringField('电子邮箱', validators=[
        DataRequired(), Length(1, 64), Email()])
    username = StringField('用户名', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^\w*$', message='用户名只能由字母数字或者下划线组成')])
    password = PasswordField('密码', validators=[
        DataRequired(), EqualTo('repassword', message='密码不一致')])
    repassword = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('注册')

    # 两个自定义的验证函数, 以validate_ 开头且跟着字段名的方法,这个方法和常规的验证函数一起调用。
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            # 自定义的验证函数要想表示验证失败,可以抛出 ValidationError 异常,其参数就是错误消息。
            raise ValidationError('电子邮箱已经注册.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经占用.')
