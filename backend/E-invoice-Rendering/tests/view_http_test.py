import pytest
import requests
import json
from src import config
from src.database import clear_users, clear_invoices, clear_bucket, access_db

@pytest.fixture
def clear_data():
    clear_users()

@pytest.fixture
def register_one_user():
    clear_invoices()
    clear_bucket()
    clear_users()
    # Register 1 user
    payload = {'name': 'Bob', 'email': 'myemail@gmail.com', 'password': 'password', 'account': 'business'}
    resp = requests.post(config.url+'auth/register', data=payload)
    return json.loads(resp.text)['api_key']

# 403 Error code (AccessError) when api key is invalid

def test_invalid_api_key(clear_data):
    # Send POST request with xml file and invalid api key
    # No users have registered
    headers = {'x-api-key': 'invalid_api_key'}
    payload = {'render_id': 1}
    resp = requests.get(config.url+'render/view', params=payload, headers=headers)

    assert resp.status_code == 403

# 403 Error code (AccessError) when api key is empty str
def test_empty_api_key(clear_data):
    # Send POST request with xml file and EMPTY api key str
    headers = {'x-api-key': ''}
    payload = {'render_id': 1}
    resp = requests.get(config.url+'render/view', params=payload, headers=headers)
    assert resp.status_code == 403

# 200 successful operation
def test_view_invoice_http(register_one_user):

    headers = {'x-api-key': register_one_user}
    files = {'xml_file': open('tests/valid_sample.xml','rb')}
    resp = requests.post(config.url+'render/html', files=files, headers=headers)

    headers = {'x-api-key': register_one_user}
    payload = {'render_id': 1}
    resp = requests.get(config.url+'render/view', params=payload, headers=headers)

    assert resp.status_code == 200
