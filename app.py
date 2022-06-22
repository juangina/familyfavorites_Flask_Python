from flask import Flask
from flask_login import LoginManager
#from flask_bootstrap import Bootstrap

#create and instance of a flask app
app = Flask(__name__)

#bind Bootstrap to the flask app
#Bootstrap(app)

app.config['SECRET_KEY'] = ''

app.config['MAIL_SERVER'] = ''
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
#app.config['MAIL_DEBUG'] = False
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_DEFAULT_SENDER'] = 'jejlifestyle@theaccidentallifestyle.net'
app.config['MAIL_MAX_EMAILS'] = None
#app.config['MAIL_SUPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False

if __name__ == '__main__':
    app.run(debug=True)

#create an instance of LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#import other modules into the app module
import routes
