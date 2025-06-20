from app.extensions import db

# create a class called items and it must inherit db.Model

class Items(db.Model):
    """ 
    Represents an item in the inventory. 
    Maps to the 'item' table in the database
    """ 

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(200))
    price = db.Column(db.Float, nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    
    def to_dict(self): 
        """
        converts the item object ot a dictionary for JSON serialization
        """
        data = {
            "id": self.id,
            "name": self.name ,
            "description": self.description,
            "price":self.price,
            "quantity": self.quantity
        }
        return data 
    
    def __repr__(self): 
        """
        provides a readble representation of the item object
        """
        
        return f"<Item {self.name} ID: {self.id}>"
    
    
    