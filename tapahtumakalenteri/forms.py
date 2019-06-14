from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField('sähköposti',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Salasana', validators=[DataRequired()])
    remember = BooleanField('Pidä minut sisäänkirjautuneena')
    submit = SubmitField('Kirjaudu')
