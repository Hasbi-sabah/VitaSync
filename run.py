from flask import Flask
from api import api
from json import JSONEncoder
from models.drug import Drug
from os import getenv

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Drug):
            # Convert Drug object to a dictionary
            return obj.__json__
        return super().default(obj)


app = Flask(__name__)
SECRET_KEY = getenv('SECRET_KEY')
print(SECRET_KEY)
app.config['SECRET_KEY'] = SECRET_KEY
app.register_blueprint(api)
app.url_map.strict_slashes = False
app.json_encoder = CustomJSONEncoder


if __name__ == '__main__':
    app.run(debug=True)
