'''this module contains functions for the server'''
from datetime import datetime
from flask import Flask, request, make_response, send_file, render_template, jsonify
from src import config
from src.track import log
from src.render import render_html, render_view
from src.database import api_key_check, render_delete, render_id_invalid, get_acc_type
from src.errors import AccessError, InputError
from src.auth import auth_register, auth_login

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/render/html", methods=['POST'])
def render_html_invoice():
    ''' Given a UBL XML invoice, return the rendered invoice in HTML format'''
    start_time = datetime.now()

    # Retrieve XML file
    xml_file = request.files['xml_file']

    # Retrieve API key from authorisation header
    api_key = request.headers['x-api-key']

    # If API key is not valid, return 403 error code
    if not api_key_check(api_key):
        log("/render/html", start_time, 403)
        raise AccessError("API key is invalid")

    # Call function
    ret = render_html(xml_file, api_key)

    # Sends file to user
    result = make_response(send_file('../invoice_render.html'))

    # Return render_id in response header
    result.headers = {'renderID': ret['render_id']}

    log("/render/html", start_time, 200)
    return result

@app.route("/auth/register", methods=['POST'])
def generate_api_key():
    ''' Given a valid email and password, register user and return personal API'''
    start_time = datetime.now()
    
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    account_type = request.form['account']

    # Checks for name, email and password are done in auth_register function
    api_key = auth_register(name, email, password, account_type)

    log("/auth/register", start_time, 200)
    return {'api_key': api_key}

@app.route("/auth/login", methods=['POST'])
def login_user():
    ''' Given a valid existing email and correct password, login user and return personal API'''
    start_time = datetime.now()

    email = request.form['email']
    password = request.form['password']

    # Checks for email and password are done in auth_login function
    api_key = auth_login(email, password)
    acc_type = get_acc_type(api_key)

    log("/auth/login", start_time, 200)
    return {'api_key': api_key, 'account_type': acc_type}

@app.route("/render/delete", methods=['DELETE'])
def delete_render():
    ''' Given the ID of a rendered invoice in the database, delete it from the database.'''
    start_time = datetime.now()

    # Retrieve API key and render id
    api_key = request.headers['x-api-key']
    render_id = request.args.get('render_id')

    # If API key is not valid, return 403 error code
    if not api_key_check(api_key):
        log("/render/delete", start_time, 403)
        raise AccessError("API key is invalid")
    # If render id doesn't exist, return 403 error code
    if render_id_invalid(render_id):
        log("/render/delete", start_time, 400)
        raise InputError("render id is invalid")

    # Delete
    render_delete(render_id, api_key)

    log("/render/delete", start_time, 200)
    return {}

@app.route("/render/view", methods=['GET'])
def view_render():
    ''' Given the ID of a rendered invoice in the database, return download link of render.'''
    start_time = datetime.now()
    # Retrieve API key from authorisation header
    api_key = request.headers['x-api-key']
    # Retrieve render ID
    render_id = request.args.get('render_id')

    # If API key is not valid, return 403 error code
    if not api_key_check(api_key):
        log("/render/view", start_time, 403)
        raise AccessError("API key is invalid")
    # If render id doesn't exist, return 400 error code
    if render_id_invalid(render_id):
        log("/render/view", start_time, 400)
        raise InputError("render id is invalid")
    url = render_view(int(render_id), api_key)
    log("/render/view", start_time, 200)
    return {'url': url}

@app.route("/healthcheck")
def check_health():
    resp = jsonify(success=True)
    return resp

if __name__ == "__main__":
    app.run(debug=False,port=config.PORT) # Do not edit this port
