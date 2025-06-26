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

# Endpoint to create items
@api_bp.route('/items', methods = ["POST"])
def create_item(): 
    
    data = request.get_json() # {}
    # basic validation 
    if not data or not all(key in data for key in ["name" , "price", "quantity"]): 
        # abort with a 400 bad request if essential data is missing 
        abort(400, description = 'missing required fields' )
    
    new_item = Items(
        name = data['name'], 
        description = data.get('description'),
        price = data['price'],
        quantity = data['quantity']
    )
    
    db.session.add(new_item)
    db.session.commit()
    
    return jsonify(new_item.to_dict()),201
    


# Endpoint to get all items 
@api_bp.route('/items', methods = ['GET'])
def get_items(): 
    """ 
    Retrieves a list of all items in the inventory
    """
    
    items = Items.query.all()

    return jsonify([item.to_dict() for item in items]),200

@api_bp.route('/items/<int:item_id>', methods = ['POST'])
def get_item(item_id):
    
    """ 
    Retrives detailes of a single item by its ID 
    """
    
    item = Items.query.get_or_404(item_id)
    return jsonify(item.to_dict()),200
    

# PUT Reuqest to update na exsiting item resrouce by its ID 
@api_bp.route("/items/<int:item_id>", methods = ["PUT"])
def update_item(item_id): 
    """updates an existing item by its ID

    Args:
        item_id (int): item id that we parse in the query param
    """
    # got the exisiting data for the db
    item = Items.query.get_or_404(item_id)
    
    # got the data that the client wants us to update in the paylod
    data = request.get_json()
    
    # checked that the data is not empty --> != {}
    if not data: 
        abort(400, description = "no data provided for update")
    
    # update fiels only if they are present in the request data. 
    item.name = data.get('name', item.name )
    item.description = data.get('description', item.description)
    item.price = data.get('price', item.price)
    item.quantity = data.get('quantity', item.quantity)
    
    # commit our update to the database
    db.session.commit()
    
    return jsonify(item.to_dict()),200
    
# Delete endpoint --> remove an item resoruce 

@api_bp.route('/items/<int:item_id>', methods =['DELETE'])
def delete_item(item_id): 
    """Delete an item from the investory by its ID

    Args:
        item_id (int): item id in the database
    """

    # Check if the data exists in the database 
    item = Items.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    
    # Return a 204 No content status for successful deletion with no response body 
    return jsonify({"message": 
        "Item deleted successfuly"}), 200
    