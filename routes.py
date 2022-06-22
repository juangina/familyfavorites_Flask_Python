from app import app, login_manager
from forms import RegistrationForm, LoginForm, FavoritesForm, ContactForm
from models import User #, Favorites
from dev.SampleData import topicObject, imageObject, quoteObject, topicsObject, favoritesObject, randArray

from werkzeug.urls import url_parse
from flask import render_template, request, url_for, flash, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required
from flask_mail import Mail
from flask_mail import Message

import psycopg2
from numpy import random
import numpy as np
import requests

t_host = ""
t_port = ""
t_dbname = ""
t_user = ""
t_pw = ""

@login_manager.user_loader
def load_user(user_id):
    #print("Login-Manager Loading Current User")
    userObject = User()
    return userObject.get_user(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return "You are not logged in. Click here to get <a href="+ str("/login")+">back to Login Page</a>"

def set_password_hash(password):
    password_hash = generate_password_hash(password)
    return password_hash

def verify_password_hash(password_hash, password):
    return check_password_hash(password_hash, password)

@app.route('/')
def index():
    username='juaneric'
    title = 'Welcome'
    return render_template('landing_page.html', loggedin=True, username=username, title=title)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    username = "juaneric"
    title = 'Registration'
    
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password_hash = set_password_hash(form.password.data)
        db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
        db_cursor = db_conn.cursor()
        db_cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s);",(username, email, password_hash))
        try:
            db_conn.commit()
        except psycopg2.Error as e:
            sql_Command = "INSERT INTO users (username, email, password)"
            t_msg = "Login: Database error: " + e + "/n SQL: " + sql_Command
            print(t_msg)   
        db_cursor.close()
        db_conn.close()

        print('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    return render_template('registration.html', loggedin=True, username=username, title=title, form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    username = 'juaneric'
    title = 'Login'

    if form.validate_on_submit():
        db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
        db_cursor = db_conn.cursor()
        db_cursor.execute("SELECT * FROM users WHERE username = %s;",(form.username.data,))   
        user_row = db_cursor.fetchone()
        db_cursor.close()
        db_conn.close()

        if user_row:
            password_hash = user_row[3]
            if(verify_password_hash(password_hash, form.password.data)):
                userObject = User()
                user = userObject.get_user(user_row[0])
                login_user(user, remember=form.remember_me.data)
                print('Congratulations, you are now logged in!')
                next_page = request.args.get('next')
                if not next_page or url_parse(next_page).netloc != '':
                    next_page = url_for('dashboard')
                return redirect(next_page)
            else:
                print('Invalid password')
        else:
            print('Invalid username')    
    return render_template('login.html', loggedin=True, username=username, title=title, form=form)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    username = "juaneric"
    title = 'Contact Me'
    
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        phone = form.phone.data
        comments = form.comments.data

        mail = Mail()
        mail.init_app(app)

        message_data = 'Username: ' + username + '\n' + 'Email: ' + email + '\n' + 'Phone: ' + phone + '\n' + 'Comments: ' + comments

        msg = Message("HI", recipients=['ericrenee21@gmail.com'] )
        msg.body = message_data
        mail.send(msg)

        print('Thank You for your Comments.  You will be contacted shortly regarding your query.')
        next_page = url_for('dashboard')
        return redirect(next_page)

    return render_template('contact.html', loggedin=True, username=username, title=title, form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = FavoritesForm()
    user = "juaneric"
    title = 'Dashboard'

    if request.method == 'POST':
        topic = request.form["topic"]
        favorite = request.form["favorite"]
        comments = request.form["comment"]
        username = "Juan Johnson"

        db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
        db_cursor = db_conn.cursor()
        
        db_cursor.execute("INSERT INTO favorites (username, topic, favorite, comments) VALUES (%s, %s, %s, %s);",(username, topic, favorite, comments))
        try:
            db_conn.commit()
            
            
        except psycopg2.Error as e:
            sql_Command = "INSERT INTO favorites (username, topic, favorite, comments)"
            t_msg = "Favorites: Database error: " + e + "/n SQL: " + sql_Command
            print(t_msg)   
        db_cursor.close()
        db_conn.close()
        #print("Form Submitted")

        return redirect(url_for('dashboard'))

    db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
    db_cursor = db_conn.cursor()
    
    db_cursor.execute("SELECT * FROM  favorite_topics;")   
    topics_Object = db_cursor.fetchall()
    topics_ObjectCount = db_cursor.rowcount
    
    db_cursor.execute("SELECT * FROM  favorites;")   
    favorites_Object = db_cursor.fetchall()
    favorites_ObjectCount = db_cursor.rowcount
    
    db_cursor.close()
    db_conn.close()

    if(topics_Object):
        #print(topics_Object)  
        if(topics_ObjectCount):
            topic_Object = topics_Object[random.randint(1,topics_ObjectCount)]
        else:
            topic_Object = topics_Object[random.randint(1,3)]
        topicsObject = list(topics_Object)
        topicObject = topic_Object

    if(favorites_Object):
        #print(favorites_Object)
        if(favorites_ObjectCount):
            randArray =[]
            for i in range(favorites_ObjectCount):
                randArray.append(i)
                
            #print(randArray)
            randArray = np.array(randArray)
            random.shuffle(randArray)
            #print(randArray)
            favoritesObject = list(favorites_Object)

    url = "https://api.pexels.com/v1/search?query=" + topicObject[1] + "&per_page=1"
    images_ObjectResponse = requests.get(url, headers = {"Authorization": "563492ad6f91700001000001e0f967773c3c4b39bac3b35ac6b5496f"})
    images_Count = images_ObjectResponse.json()['total_results']
    #print(images_Count)

    imageIndex = random.randint(1, images_Count)
    url = "https://api.pexels.com/v1/search?page=" + str(imageIndex) + "&query=" + topicObject[1] + "&per_page=1"
    image_ObjectResponse = requests.get(url, headers = {"Authorization": "563492ad6f91700001000001e0f967773c3c4b39bac3b35ac6b5496f"})
    image_Object = image_ObjectResponse.json()
    #print(image_Object)

    if(image_Object):
        imageObject = image_Object
        #print(imageObject['page'])

    url = "https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json&jsonp=?"
    quote_ObjectResponse = requests.get(url)
    quote_Object = quote_ObjectResponse.json()
    #print(quote_Object)

    if(quote_Object):
        quoteObject = quote_Object
        #print(quoteObject['quoteText'])
    
    return render_template('dashboard.html', loggedin=True, username=user, title=title, form=form, topicObject=topicObject, imageObject=imageObject, quoteObject=quoteObject, topicsObject=topicsObject, favoritesObject=favoritesObject, randArray=randArray)


@app.route('/trivia')
@login_required
def trivia():
    username = "juaneric"
    title = 'Trivia'

    return render_template('trivia.html', loggedin=True, username=username, title=title)

@app.route('/products', methods=['GET', 'POST'])
@login_required
def products():
    username = "juaneric"
    title = 'Products'

    return render_template('products.html', loggedin=True, username=username, title=title)

@app.route('/debug', methods=['GET', 'POST'])
@login_required
def debug():
    username = "juaneric"
    title = 'Debug Out'

    return render_template('debug.html', loggedin=True, username=username, title=title)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))