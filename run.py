from datetime import datetime
from flask import Flask
from flask_cors import CORS
from api import api
from json import JSONEncoder
from models.drug import Drug
from os import getenv
import schedule
import time
from api.base import check_appointments


app = Flask(__name__, static_url_path='/assets', static_folder='assets')
host = getenv('API_HOST') or "localhost"
port = getenv('API_PORT') or 5000
SECRET_KEY = getenv('SECRET_KEY')
SMTP_EMAIL = getenv('SMTP_EMAIL')
SMTP_API_KEY = getenv('SMTP_API_KEY')
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SMTP_EMAIL'] = SMTP_EMAIL
app.config['SMTP_API_KEY'] = SMTP_API_KEY
app.register_blueprint(api)
app.url_map.strict_slashes = False
cors_config = {
    "origins": ["http://localhost:5000", "http://localhost:4000"]
}
CORS(app, **cors_config)
app.jinja_env.globals.update(datetime=datetime)


def job_scheduler():
    # loop to make sure jobs run continuously
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    """Run the app in debug mode."""
    app.run(debug=True, host=host, port=port)

    # times we run the jobs
    schedule.every().day.at("11:00").do(check_appointments)
    schedule.every().day.at("16:00").do(check_appointments)
    # shcedule the job scheduler
    job_scheduler()
