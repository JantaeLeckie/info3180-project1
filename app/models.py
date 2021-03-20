from . import db 

class Property(db.Model):
    property_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    property_title = db.Column(db.String(50))
    property_description = db.Column(db.String(255))
    property_rooms = db.Column(db.String(255))
    property_bathrooms = db.Column(db.String(255))
    property_price = db.Column(db.String(255))
    property_type = db.Column(db.String(20))
    property_location = db.Column(db.String(255))
    property_photo = db.Column(db.String(255))

    def __init__(self, property_name, property_description, property_rooms, property_bathroom, property_price, property_type, property_location, property_photo):
        self.property_name = property_name
        self.property_description = property_description
        self.property_rooms = property_rooms
        self.property_bathroom = property_bathroom
        self.property_price = property_price  
        self.property_type = property_type  
        self.property_location = property_location
        self.property_photo = property_photo    