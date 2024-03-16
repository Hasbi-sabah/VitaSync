from flask import Flask
from flask_cors import CORS
from os import getenv


app = Flask(__name__)
host = getenv('APP_HOST') or "localhost"
port = getenv('APP_PORT') or 3500
SECRET_KEY = getenv('SECRET_KEY')
print(SECRET_KEY)
app.config['SECRET_KEY'] = SECRET_KEY
app.register_blueprint(api)
app.url_map.strict_slashes = False
cors_config = {
    "origins": ["http://localhost:5000", "http://localhost:4000"]
}
CORS(app, **cors_config)


if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)
