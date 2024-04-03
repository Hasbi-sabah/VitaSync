from datetime import datetime
from flask import Flask
from flask_cors import CORS
from api import api
from os import getenv
import schedule
import threading
import time
from api.base import check_appointments


# Create the Flask app
# Create the Flask app
app = Flask(__name__, static_url_path='/assets', static_folder='assets')

# Get environment variables or use defaults

# Get environment variables or use defaults
host = getenv('API_HOST') or "localhost"
port = getenv('API_PORT') or 5000
SECRET_KEY = getenv('SECRET_KEY')
SMTP_EMAIL = getenv('SMTP_EMAIL')
SMTP_API_KEY = getenv('SMTP_API_KEY')

# Configure Flask app settings

# Configure Flask app settings
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SMTP_EMAIL'] = SMTP_EMAIL
app.config['SMTP_API_KEY'] = SMTP_API_KEY

# Register the API blueprint

# Register the API blueprint
app.register_blueprint(api)

# Allow cross-origin resource sharing (CORS)
# dev routes for frontend, to be removed in production
# as one link will take over
cors_config = {
    "origins": [
        "http://vitasync.me",
        "https://vitasync.pagekite.me",
        "https://api-vitasync.pagekite.me",
        "https://doc-vitasync.pagekite.me",
        "https://nurse-vitasync.pagekite.me",
        "https://patient-vitasync.pagekite.me",
        "https://pharmacy-vitasync.pagekite.me",
        ],
    "supports_credentials": True
}
CORS(app, **cors_config)

# Update Jinja environment with custom global functions

# Update Jinja environment with custom global functions
app.jinja_env.globals.update(datetime=datetime)

# Define job function to be scheduled
def run_job():
    with app.app_context():
        check_appointments()

# Define job_scheduler function to run scheduled jobs continuously
def job_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start the scheduler in a separate thread
scheduler_thread = threading.Thread(target=job_scheduler)
scheduler_thread.start()

# Run the Flask app in debug mode
if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True, host=host, port=port)
