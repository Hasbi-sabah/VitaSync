from flask import render_template, redirect, request, jsonify, make_response
from flask import Blueprint
import requests

main_routes = Blueprint('main_routes', __name__, template_folder='../../public/templates')

def check_token():
    """Check if JWT token is present in cookies."""
    token = request.cookies.get('jwt_token')
    return token is not None

@main_routes.route('/')
def index():
    """Render index page if JWT token is present in cookies."""
    if not check_token():
        return redirect('/login')
    return render_template('index.html')

@main_routes.route('/login', methods=['GET', 'POST'])
def login():
    """Render login page if JWT token is not present in cookies. Handle login form submission."""
    if request.method == 'POST':
        """Capture form data and send to login API."""
        username = request.form['username']
        password = request.form['password']

        login_data = {'username': username, 'password': password}
        response = requests.post('http://localhost:5000/api/login', json=login_data)
        if response.status_code == 200:
            """If login is successful, set JWT token in cookies."""
            new_token = response.json().get('token')
            response = make_response(redirect('/'))
            response.set_cookie('jwt_token', new_token)
            return response
        else:
            """If login fails, return error message."""
            return redirect('/login')
    return render_template('login.html')

# routes for prescription
@main_routes.route('/prescription/<uuid:prescriptionId>', methods=['GET'])
def get_prescription(prescriptionId):
    """Retrieve prescription details."""
    jwt_token = request.cookies.get('jwt_token')
    response = requests.get(f'http://localhost:5000/api/prescription/{prescriptionId}', headers={'Authorization': f'Bearer {jwt_token}'})
    if response.status_code == 200:
        prescription_data = response.json()
        return render_template('prescription.html', prescription=prescription_data)
    elif response.status_code == 404:
        return render_template('error.html', message='Prescription not found'), 404
    elif response.status_code == 401:  # Invalid token
        return redirect('/login')
    else:
        return render_template('error.html', message='An error occurred'), 500

@main_routes.route('/prescription/<uuid:prescriptionId>/fill', methods=['GET'])
def fill_prescription(prescriptionId):
    """Fill a prescription."""
    jwt_token = request.cookies.get('jwt_token')
    response = requests.get(f'http://localhost:5000/api/prescription/{prescriptionId}/fill', headers={'Authorization': f'Bearer {jwt_token}'})
    if response.status_code == 200:
        prescription_data = response.json()
        return render_template('prescription.html', prescription=prescription_data)
    elif response.status_code == 404:
        return render_template('error.html', message='Prescription not found'), 404
    elif response.status_code == 409:
        return render_template('error.html', message='Prescription already filled'), 409
    elif response.status_code == 401:  # Invalid token
        return redirect('/login')
    else:
        return render_template('error.html', message='An error occurred'), 500

@main_routes.route('/prescription/<uuid:prescriptionId>', methods=['PUT'])
def update_prescription(prescriptionId):
    """Update prescription details."""
    jwt_token = request.cookies.get('jwt_token')
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    response = requests.put(f'http://localhost:5000/api/prescription/{prescriptionId}', json=data, headers={'Authorization': f'Bearer {jwt_token}'})
    if response.status_code == 200:
        prescription_data = response.json()
        return render_template('prescription.html', prescription=prescription_data)
    elif response.status_code == 404:
        return render_template('error.html', message='Prescription not found'), 404
    elif response.status_code == 401:  # Invalid token
        return redirect('/login')
    else:
        return render_template('error.html', message='An error occurred'), 500

@main_routes.route('/prescription/<uuid:prescriptionId>', methods=['DELETE'])
def delete_prescription(prescriptionId):
    """Delete a prescription."""
    jwt_token = request.cookies.get('jwt_token')
    response = requests.delete(f'http://localhost:5000/api/prescription/{prescriptionId}', headers={'Authorization': f'Bearer {jwt_token}'})
    if response.status_code == 200:
        return jsonify({}), 200
    elif response.status_code == 404:
        return render_template('error.html', message='Prescription not found'), 404
    elif response.status_code == 401:  # Invalid token
        return redirect('/login')
    else:
        return render_template('error.html', message='An error occurred'), 500

# Routes for records
@main_routes.route('/record/<uuid:recordId>', methods=['GET'])
def get_record_view(recordId):
    """Retrieve record details."""
    jwt_token = request.cookies.get('jwt_token')
    response = requests.get(f'http://localhost:5000/api/record/{recordId}', headers={'Authorization': f'Bearer {jwt_token}'})
    if response.status_code == 200:
        record_data = response.json()
        return render_template('record.html', record=record_data)
    elif response.status_code == 404:
        return render_template('error.html', message='Record not found'), 404
    elif response.status_code == 401:  # Invalid token
        return redirect('/login')
    else:
        return render_template('error.html', message='An error occurred'), 500

@main_routes.route('/record/<uuid:recordId>/edit', methods=['GET'])
def edit_record(recordId):
    """Render page to edit record."""
    jwt_token = request.cookies.get('jwt_token')
    response = requests.get(f'http://localhost:5000/api/record/{recordId}', headers={'Authorization': f'Bearer {jwt_token}'})
    if response.status_code == 200:
        record_data = response.json()
        return render_template('edit_record.html', record=record_data)
    elif response.status_code == 404:
        return render_template('error.html', message='Record not found'), 404
    elif response.status_code == 401:  # Invalid token
        return redirect('/login')
    else:
        return render_template('error.html', message='An error occurred'), 500

@main_routes.route('/record/<uuid:recordId>/update', methods=['POST'])
def update_record(recordId):
    """Update record details."""
    jwt_token = request.cookies.get('jwt_token')
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = request.get_json()
    else:
        data = request.form.to_dict()
    response = requests.put(f'http://localhost:5000/api/record/{recordId}', json=data, headers={'Authorization': f'Bearer {jwt_token}'})
    if response.status_code == 200:
        record_data = response.json()
        return redirect(f'/record/{recordId}')
    elif response.status_code == 404:
        return render_template('error.html', message='Record not found'), 404
    elif response.status_code == 401:  # Invalid token
        return redirect('/login')
    else:
        return render_template('error.html', message='An error occurred'), 500

@main_routes.route('/record/<uuid:recordId>/delete', methods=['POST'])
def delete_record(recordId):
    """Delete a record."""
    jwt_token = request.cookies.get('jwt_token')
    response = requests.delete(f'http://localhost:5000/api/record/{recordId}', headers={'Authorization': f'Bearer {jwt_token}'})
    if response.status_code == 200:
        return redirect('/')
    elif response.status_code == 404:
        return render_template('error.html', message='Record not found'), 404
    elif response.status_code == 401:  # Invalid token
        return redirect('/login')
    else:
        return render_template('error.html', message='An error occurred'), 500
