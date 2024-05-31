from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


# Initialize SQLAlchemy 
db = SQLAlchemy()

# Initialize Bcrypt 
bcrypt = Bcrypt()

# Initialize LoginManager 
login_manager = LoginManager()

login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

# Initialize Mail 
mail = Mail()


# Create a application function that allows us to create different instances of our application
def create_app(config_class=Config):
    # Initialize Flask application
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Import routes to register them with the app
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes  import main
    from flaskblog.errors.handlers import errors

    # Register the Blueprint
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app