from app import create_app , db
from app.models import Items # we import models so db.create_all() knows about them.

app = create_app()
app2 = create_app()

if __name__ == '__main__': 
    with app.app_context(): 
        db.create_all()  # Creates the databse table if they do not exist 
    
    app.run(debug= True)
         