from app.extensions import db 
from app.config import Config 
from app.routes.api import api_bp

from flask import Flask


def create_app(config_class = Config): 
    """ 
    Create and congigure the flask application 
    Uses the applciationf actory pattern for flexibility
    """
    
    app = Flask(__name__)
    app.config.from_object(config_class)
            
    # initalise extensions with the app 
    db.init_app(app)
    
    # Register API blueprints 
    # The urls prexit is already defined in the BP itself 
    app.register_blueprint(api_bp)
    
    return app