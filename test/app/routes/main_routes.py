from flask import Blueprint, render_template, redirect, request, jsonify, make_response
import requests

main_routes = Blueprint('main_routes', __name__, template_folder='../../public/templates')

def check_token():
    """check if JWT token is present in cookies."""
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
    """Render login page if JWT token is not present in cookies. 
    handle login form submission."""
    if request.method == 'POST':
        """capture form data and send to login API."""
        username = request.form['username']
        password = request.form['password']

        login_data = {'username': username, 'password': password}
        response = requests.post('http://localhost:5000/api/login', json=login_data)
        if response.status_code == 200:
            """if login is successful, set JWT token in cookies."""
            new_token = response.json().get('token')
            response = make_response(redirect('/'))
            response.set_cookie('jwt_token', new_token)
            return response
        else:
            """if login fails, return error message."""
            return redirect('/login')
    return render_template('login.html')
