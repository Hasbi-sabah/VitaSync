from datetime import datetime
from flask import Flask
from flask_cors import CORS
from api import api
from os import getenv
import schedule
import time
from api.base import check_appointments


# Create the Flask app
app = Flask(__name__, static_url_path='/assets', static_folder='assets')

# Get environment variables or use defaults
host = getenv('API_HOST') or "localhost"
port = getenv('API_PORT') or 5000
SECRET_KEY = getenv('SECRET_KEY')
SMTP_EMAIL = getenv('SMTP_EMAIL')
SMTP_API_KEY = getenv('SMTP_API_KEY')

# Configure Flask app settings
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SMTP_EMAIL'] = SMTP_EMAIL
app.config['SMTP_API_KEY'] = SMTP_API_KEY

# Register the API blueprint
app.register_blueprint(api)

# Allow cross-origin resource sharing (CORS)
cors_config = {
    "origins": ["http://localhost:5000", "http://localhost:3000", "http://localhost:3001", "http://localhost:3002", "http://localhost:3003"],
    "supports_credentials": True
}
CORS(app, **cors_config)

# Update Jinja environment with custom global functions
app.jinja_env.globals.update(datetime=datetime)

# Define job_scheduler function to run scheduled jobs continuously
def job_scheduler():
    while True:
        with app.app_context():
            schedule.run_pending()
        time.sleep(1)

# Define the job function to be scheduled
def run_job(app):
    with app.app_context():
        check_appointments()

if __name__ == '__main__':
    """Run the app in debug mode."""
    # Schedule job to run at specific time daily
    schedule.every().day.at("16:00").do(run_job, app)
    
    # Start the job scheduler
    job_scheduler()
    
    # Run the Flask app in debug mode
    app.run(debug=True, host=host, port=port)
