from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from .forms import  LoginForm, FilmForm ,RegistrationForm ,FiltresForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'


class Admin (db.Model, UserMixin):
    id= db.Column (db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    password=db.Column(db.String, nullable=False)

    def hash_password(self, password):
        self.password= generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password, password)


class PostFilm (db.Model):
    name=db.Column (db.String, nullable=False)
    id=db.Column (db.Integer, primary_key=True)
    genre=db.Column (db.String, nullable=False)
    text=db.Column (db.Text, nullable=False)
    actor=db.Column (db.String, nullable=False)
    data=db.Column (db.Integer, nullable=False)
    rating=db.Column (db.String, nullable=False)
    time=db.Column(db.String, nullable=False)
    photo=db.Column(db.String, nullable=False)


@login.user_loader
def userLoader(id):
    return Admin.query.get(id)


@app.route('/Adminreg', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return redirect('/')
    return render_template("Admin.html", form=form)


@app.route("/Admin", methods=['GET', 'POST'])
def LoginForm():
    form=RegistrationForm()
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        username1=Admin.query.filter_by(name=username).first()
        if username1 is None or not username1.check_password(password):
            return redirect ("/Admin")
        login_user(username1)
        return redirect('/')
    return render_template("Admin.html", form=form)


@app.route("/Creat", methods=['GET', 'POST'])
def creat():
    form =FilmForm()
    if form.validate_on_submit():
        name=form.name.data
        actor=form.actor.data
        text=form.text.data
        data=form.data.data
        rating=form.rating.data
        time=form.time.data
        genre=form.genre.data
        photo=form.photo.data
        photo.save(f'app/static/zobra/{photo.filename}')
        clas=PostFilm(name=name,actor=actor,text=text,data=data,rating=rating,time=time,genre=genre,photo=f'/static/zobra/{photo.filename}',)#закидую інфу в колонку
        db.session.add(clas)
        db.session.commit()
        return redirect('/')
    return render_template("film_info.html", form=form)


@app.route("/", methods=['GET', 'POST'])
def fers():
    al=PostFilm.query.all()
    return render_template("home.html", al=al)


@app.route("/filminfo<int:filmt>", methods=['GET', 'POST'])
def filminfo(filmt):
    alle=PostFilm.query.get(filmt)
    return render_template("infoforfilms.html", alle=alle)


@app.route("/filtres", methods=['GET', 'POST'])
def filtres():
    filters=FiltresForm()
    if filters.validate_on_submit():
        genre=filters.genre.data
        time=filters.time.data
        if genre!='' and time=='':
            filt=PostFilm.query.filter_by(genre=genre)
        elif genre=='' and time!='':
            filt=PostFilm.query.filter_by(data=time)
        else:
            filt = PostFilm.query.filter_by(data=time,genre=genre)
        print(filt)
        return render_template("filter.html", filt=filt, filters=filters)
    return render_template("filter.html", filters=filters)