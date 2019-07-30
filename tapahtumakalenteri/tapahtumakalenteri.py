from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678'


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='register', form=form)


@app.route("/uusitapahtuma")
def uusitapahtuma():
    return render_template('uusitapahtuma.html', title='uusitapahtuma')


if __name__ == '__main__':
    app.run(debug=True)
