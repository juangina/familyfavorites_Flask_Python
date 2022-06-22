from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField, Label
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import psycopg2

t_host = ""
t_port = ""
t_dbname = ""
t_user = ""
t_pw = ""

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Username"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Repeat Password"})
    submit = SubmitField('Register')

    def validate_username(self, username):
        print("Username: " + username.data)
        db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
        db_cursor = db_conn.cursor()
        #sql_scripts_find = "SELECT * FROM users WHERE username = {} LIMIT 1;".format(username.data)
        #db_cursor.execute(sql_scripts_find)
        db_cursor.execute("SELECT * FROM users WHERE username = %s;",(username.data,))   
        user = db_cursor.fetchone()
        db_cursor.close()
        db_conn.close()

        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        print("Email: " + email.data)
        db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
        db_cursor = db_conn.cursor()
        #sql_scripts_find = "SELECT * FROM users WHERE email = {} LIMIT 1;".format(email.data)
        #db_cursor.execute(sql_scripts_find)
        db_cursor.execute("SELECT * FROM users WHERE email = %s;",(email.data,))
        email = db_cursor.fetchone()
        db_cursor.close()
        db_conn.close()
    
        if email is not None:
            raise ValidationError('Please use a different email address.')
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class FavoritesForm(FlaskForm):
    topic = StringField('Topic', validators=[DataRequired()], render_kw={"placeholder": "Topic"})
    description = StringField('Description', validators=[DataRequired()], render_kw={"placeholder": "Description"})
    user = StringField('User', validators=[DataRequired()], render_kw={"placeholder": "User"})
    comments = StringField('Comments', validators=[DataRequired()], render_kw={"placeholder": "Comments"})
    submit = SubmitField('Submit')

class ContactForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Username"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    phone = StringField('Phone', render_kw={"placeholder": "Phone Number"})
    #comments_label = Label(field_id="Comments", text="Comments")
    comments = TextAreaField('Comments', render_kw={"placehoder": "Comments"})
    submit = SubmitField('Submit')
