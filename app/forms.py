from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, IntegerField, TextField, FloatField, FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField,FileRequired,FileAllowed 

from flask.helpers import send_from_directory

class PropertyFrom(FlaskForm):
    title =  TextField("Property Title", validators = [DataRequired()])
    description = TextAreaField("Description", validators = [DataRequired()])
    rooms = TextField("No. of Rooms", validators = [DataRequired()])
    bath = TextField("No. of Bathrooms", validators = [DataRequired()])
    price = TextField("Price", validators = [DataRequired()])
    ptype = SelectField("Property Type", choices=[('House', 'House'), ('Apartment', 'Apartment')], validators = [DataRequired()]) 
    location = TextField("Location", validators = [DataRequired()])
    photo = FileField("Photo", validators=[FileRequired(), FileAllowed(['jpg','png'])])