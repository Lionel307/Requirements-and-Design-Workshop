import pytest
import requests
import json
from src import config
from src.database import clear_users

@pytest.fixture
def register_users():
    clear_users()

    # Register user 1
    payload = {'name': 'Bob', 'email': 'myemail1@gmail.com', 'password': 'password1', 'account': 'business'}
    resp = requests.post(config.url+'auth/register', data=payload)
    key1 = json.loads(resp.text)['api_key']

    # Register user 2
    payload = {'name': 'Jake', 'email': 'myemail2@gmail.com', 'password': 'password2', 'account': 'business'}
    resp = requests.post(config.url+'auth/register', data=payload)
    key2 = json.loads(resp.text)['api_key']

    # Register user 3
    payload = {'name': 'Tom', 'email': 'myemail3@gmail.com', 'password': 'password3', 'account': 'individual'}
    resp = requests.post(config.url+'auth/register', data=payload)
    key3 = json.loads(resp.text)['api_key']

    return [key1, key2, key3]

# Test successful logins returns correct api keys
def test_return_api_key(register_users):
    payload = {'email': 'myemail1@gmail.com', 'password': 'password1'}
    resp = requests.post(config.url+'auth/login', data=payload)
    assert resp.status_code == 200
    assert json.loads(resp.text) == {'api_key': register_users[0], 'account_type': 'business'}

    payload = {'email': 'myemail2@gmail.com', 'password': 'password2'}
    resp = requests.post(config.url+'auth/login', data=payload)
    assert resp.status_code == 200
    assert json.loads(resp.text) == {'api_key': register_users[1], 'account_type': 'business'}

    payload = {'email': 'myemail3@gmail.com', 'password': 'password3'}
    resp = requests.post(config.url+'auth/login', data=payload)
    assert resp.status_code == 200
    assert json.loads(resp.text) == {'api_key': register_users[2], 'account_type': 'individual'}

# Test if email inputted is not a correct email (format wise) returns InputError
def test_email_invalid(register_users):
    payload = {'email': 'myemail', 'password': 'password'}
    resp = requests.post(config.url+'auth/login', data=payload)
    assert resp.status_code == 400

    payload = {'email': '@mail.com', 'password': 'password'}
    resp = requests.post(config.url+'auth/login', data=payload)
    assert resp.status_code == 400

    payload = {'email': '', 'password': 'password'}
    resp = requests.post(config.url+'auth/login', data=payload)
    assert resp.status_code == 400
    
    payload = {'email': '', 'password': ''}
    resp = requests.post(config.url+'auth/login', data=payload)
    assert resp.status_code == 400

# Test if email does not exist/not registered returns InputError
def test_email_not_exist(register_users):
    payload = {'email': 'fake@gmail.com', 'password': 'password123'}
    resp = requests.post(config.url+'auth/login', data=payload)
    assert resp.status_code == 400
    
    payload = {'email': 'myemail@gmail.com', 'password': 'password1'}
    resp = requests.post(config.url+'auth/login', data=payload)
    assert resp.status_code == 400

# Test if password is empty returns InputError
def test_password_not_empty(register_users):
    payload = {'email': 'myemail@gmail.com', 'password': ''}
    resp = requests.post(config.url+'auth/login', data=payload)
    assert resp.status_code == 400

    payload = {'email': 'myemail1@gmail.com', 'password': ''}
    resp = requests.post(config.url+'auth/login', data=payload)
    assert resp.status_code == 400

# Test if password is incorrect for valid email returns AccessError
def test_user_storage(register_users):    
    payload = {'email': 'myemail1@gmail.com', 'password': 'incorrectPass'}
    resp = requests.post(config.url+'auth/login', data=payload)
    assert resp.status_code == 403
    
    payload = {'email': 'myemail2@gmail.com', 'password': 'password1'}
    resp = requests.post(config.url+'auth/login', data=payload)
    assert resp.status_code == 403