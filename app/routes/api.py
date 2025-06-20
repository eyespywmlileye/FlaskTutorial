from flask import Blueprint , request , jsonify , abort 
from app.models import Items
from app.extensions import db 

# define the blueprint for our api routes 

# all routes defined here will be prefixed with /api
api_bp = Blueprint('api', 
                  __name__, 
                  url_prefix = '/api')

# A simple status endpoint to cofnim the api is running 
@api_bp.route('/status' , methods = ['GET'])
def status(): 
    return jsonify({
        "status": "ok", 
        "message": "Inventory API is running"
    }),200