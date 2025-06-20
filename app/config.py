import os
from dotenv import load_dotenv

# Load our env variables into the current script
load_dotenv()

class Config(): 
    """
    Base configuration class for the Flask Application
    """
    
    #use an env variable for the data url
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    
    # needed for sessions/forms
    SECRET_KEY = os.getenv("SECRET_KEY")
    
    # Disable flask-sqlalchemy event system
    SQLALCHEMY_TRACK_MODIFICATIONS = False 