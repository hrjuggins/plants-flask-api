from application import db
from application import Plant

import json
import pprint

json_data = None
with open('data.txt', 'r') as f:
    data = f.read()
    json_data = json.loads(data)
    for row in json_data:
        name = row
        href = json_data[row]['href']
        description = json_data[row]['Description']
        picture = json_data[row]['picture']
        origin = json_data[row]['Origin:']
        names = json_data[row]['Names:']
        try:
            temperature = json_data[row]['Temperature:']
        except KeyError as E:
            pass
        light = json_data[row]['Light:']
        watering = json_data[row]['Watering:']
        try:
            soil = json_data[row]['Soil:']
        except Exception as E:
            pass
        try:
            repotting = json_data[row]['Re-Potting:']
        except Exception as E:
            pass
        try:
            fertilizer = json_data[row]['Fertilizer:']
        except Exception as E:
            pass
        try:
            humidity = json_data[row]['Humidity:']
        except Exception as E:
            pass

        new_plant = Plant(name, href, description, picture,\
            origin, names, temperature, light, watering, soil,\
            repotting, fertilizer, humidity)

        db.session.add(new_plant)

    db.session.commit()