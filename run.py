from datetime import datetime
from flask import Flask
from flask_cors import CORS
from api import api
from json import JSONEncoder
from models.drug import Drug
from os import getenv


app = Flask(__name__)
host = getenv('API_HOST') or "localhost"
port = getenv('API_PORT') or 5000
SECRET_KEY = getenv('SECRET_KEY')
print(SECRET_KEY)
app.config['SECRET_KEY'] = SECRET_KEY
app.register_blueprint(api)
app.url_map.strict_slashes = False
cors_config = {
    "origins": ["http://localhost:5000", "http://localhost:4000"]
}
CORS(app, **cors_config)
app.jinja_env.globals.update(datetime=datetime)


if __name__ == '__main__':
    """Run the app in debug mode."""
    app.run(debug=True, host=host, port=port)
