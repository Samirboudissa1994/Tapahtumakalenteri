from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):

    email = StringField('sähköposti', validators=[DataRequired(), Email()])

    password = PasswordField('Salasana', validators=[DataRequired()])
    confirm_password = PasswordField('Salasana uudelleen',
                                     validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Luo tunnus')


class LoginForm(FlaskForm):
    email = StringField('sähköposti',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Salasana', validators=[DataRequired()])
    remember = BooleanField('Pidä minut sisäänkirjautuneena')
    submit = SubmitField('Kirjaudu')
    submit2 = SubmitField('Tee tunnus')
