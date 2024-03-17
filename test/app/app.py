from flask import Flask
from flask_cors import CORS
from os import getenv
from routes.main_routes import main_routes

app = Flask(__name__, template_folder='public/templates')
app.register_blueprint(main_routes)

host = getenv('APP_HOST') or "localhost"
port = getenv('APP_PORT') or 3500
SECRET_KEY = getenv('SECRET_KEY')
app.config['SECRET_KEY'] = SECRET_KEY
app.url_map.strict_slashes = False
cors_config = {
    "origins": ["http://localhost:5000", "http://localhost:4000"]
}
CORS(app, **cors_config)

if __name__ == '__main__':
    """Run the app in debug mode."""
    app.run(debug=True, host=host, port=port)
