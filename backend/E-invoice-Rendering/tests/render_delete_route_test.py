import json
import pytest
import requests
from src import config
from src.database import clear_users, clear_invoices, clear_bucket, render_id_invalid

# Creates 2 users, each renders 1 html
@pytest.fixture
def register_two():
    clear_users()
    clear_bucket()
    clear_invoices()
    
    # Register user 1
    payload = {'name': 'Bob', 'email': 'myemail1@gmail.com', 'password': 'password1', 'account': 'business'}
    resp1 = requests.post(config.url+'auth/register', data=payload)

    # Register user 2
    payload = {'name': 'Jake', 'email': 'myemail2@gmail.com', 'password': 'password2', 'account': 'business'}
    resp2 = requests.post(config.url+'auth/register', data=payload)

    key1 = json.loads(resp1.text)['api_key']
    key2 = json.loads(resp2.text)['api_key']

    # User 1 renders a html
    headers = {'x-api-key': key1}
    files = {'xml_file': open('tests/valid_sample.xml','rb')}
    requests.post(config.url+'render/html', files=files, headers=headers)

    # User 2 renders a html
    headers = {'x-api-key': key2}
    files = {'xml_file': open('tests/valid_sample.xml','rb')}
    requests.post(config.url+'render/html', files=files, headers=headers)

    return [key1, key2]

# AccessError if api key is not input
def test_empty_api_key(register_two):
    headers = {'x-api-key': ''}
    payload = {'render_id': 1}
    resp = requests.delete(config.url + 'render/delete', params=payload, headers=headers)
    print(resp)
    assert resp.status_code == 403

# Test response status if valid user deletes own invoice
def test_valid_return(register_two):
    headers = {'x-api-key': register_two[0]}
    print(render_id_invalid(1))
    payload = {'render_id': 1}
    resp = requests.delete(config.url + 'render/delete', params=payload, headers=headers)
    assert resp.status_code == 200

# Test response status if valid user attempts to delete an invoice that's not theirs
def test_access_error(register_two):
    headers = {'x-api-key': register_two[0]}
    payload = {'render_id': 2}
    resp = requests.delete(config.url + 'render/delete', params=payload, headers=headers)
    assert resp.status_code == 403

# InputError if render id is invalid
def test_invalid_render_id(register_two):
    headers = {'x-api-key': register_two[0]}
    payload = {'render_id': 3}
    resp = requests.delete(config.url + 'render/delete', params=payload, headers=headers)
    assert resp.status_code == 400