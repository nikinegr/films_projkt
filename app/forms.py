from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, SelectField, IntegerField , FileField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    button = SubmitField('Enter')


class FilmForm(FlaskForm):
    button = SubmitField('Enter')
    name = StringField('name', validators=[DataRequired()])
    actor = StringField('actor', validators=[DataRequired()])
    text = StringField('text', validators=[DataRequired()])
    data = IntegerField('data', validators=[DataRequired()])
    rating = IntegerField('rating', validators=[DataRequired()])
    time = StringField('time', validators=[DataRequired()])
    genre = SelectField('rating',choices=[('comedia','comedia'),('boevik','boevik'),('prigodi','prigodi'),('dramma','dramma'),('katostrofa','katostrofa')], validators=[DataRequired()])
    photo = FileField('photo', validators=[FileRequired()])


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    button = SubmitField('Enter')


class FiltresForm(FlaskForm):
    genre = SelectField('rating', choices=[('comedia', 'comedia'), ('boevik', 'boevik'), ('prigodi', 'prigodi'),('dramma', 'dramma'), ('katostrofa', 'katostrofa')])
    time = SelectField('rating', choices=[('2023', '2023'), ('2022', '2022'), ('2021', '2021'), ('2020', '2020'), ('2019', '2019'), ('2018', '2018'), ('2017', '2017'), ('2016', '2016'), ('2015', '2015'), ('2014', '2014')])
    button = SubmitField('Enter')
