from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init App
application = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(application)
# Init marshmallow
ma = Marshmallow(application)

# Class/ Model
class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    href = db.Column(db.String(200))
    description = db.Column(db.String(200))
    picture = db.Column(db.String(200))
    origin = db.Column(db.String(200))
    names = db.Column(db.String(200))
    temperature = db.Column(db.String(200))
    light = db.Column(db.String(200))
    watering = db.Column(db.String(200))
    soil = db.Column(db.String(200))
    repotting = db.Column(db.String(200))
    fertilizer = db.Column(db.String(200))
    humidity = db.Column(db.String(200))

    def __init__(self, name, href, description, picture,\
        origin, names, temperature, light, watering, soil,\
        repotting, fertilizer, humidity):
        self.name = name
        self.href = href
        self.description = description
        self.picture = picture
        self.origin = origin
        self.names = names
        self.temperature = temperature
        self.light = light
        self.watering = watering
        self.soil = soil
        self.repotting = repotting
        self.fertilizer = fertilizer
        self.humidity = humidity

# Schema
class PlantSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'href', 'description', 'picture',\
            'origin', 'names', 'temperature', 'light', 'watering',\
            'soil', 'repotting', 'fertilizer', 'humidity')

#  Init schema
plant_schema = PlantSchema()
plants_schema = PlantSchema(many=True)

# Default route
@application.route('/', methods=['GET'])
def home():
    return '/plants for all plants or /plants?name= for getting specific plant by name or /plant/id for specific plant by id'


# Get all plants or plant by name
@application.route('/plants', methods=['GET'])
def get_plants():
    name = request.args.get('name', None)
    if name:
        plant = Plant.query.filter_by(name=name).first()
        return plant_schema.jsonify(plant)
    
    all_plants = Plant.query.all()
    result = plants_schema.dump(all_plants)
    return jsonify(result)

# Get single plant
@application.route('/plants/<id>', methods=['GET'])
def get_plant(id):
    plant = Plant.query.get(id)
    return plant_schema.jsonify(plant)


# Run server
if __name__ == "__main__":
    application.run(debug=True)