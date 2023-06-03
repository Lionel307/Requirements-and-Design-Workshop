import pytest
import requests
import magic
import os
from src.errors import AccessError, InputError
from src.render import render_html, render_view
from src.auth import auth_register
from src.database import clear_users, clear_invoices, clear_bucket, access_db
from pymongo import MongoClient

@pytest.fixture
def clear_data():
    clear_invoices()
    clear_bucket()
    clear_users()

def test_view_errors(clear_data):
    with pytest.raises(InputError):
        assert render_view(1, False)
    with pytest.raises(AccessError):
        assert render_view(1, '52519517682584b1848886a1d25e4027bda2dc6db9802c35ffc5d81f8a36217d')
    with pytest.raises(InputError):
        assert render_view('hello', '52519517682584b1848886a1d25e4027bda2dc6db9802c35ffc5d81f8a36217d')
    api_key1 = auth_register('Bob', "myemail@gmail.com", "password", 'business')
    api_key2 = auth_register('Jake', "myemai@gmail.com", "passwor", 'business')
    render_html("tests/valid_sample.xml", '52519517682584b1848886a1d25e4027bda2dc6db9802c35ffc5d81f8a36217d')
    with pytest.raises(AccessError):
        assert render_view(1, api_key2)

def test_render_view(clear_data):
    auth_register('Bob', "myemail@gmail.com", "password", 'business')
    render_html("tests/valid_sample.xml", '52519517682584b1848886a1d25e4027bda2dc6db9802c35ffc5d81f8a36217d')
    collection = access_db()
    invoice = collection.find_one({'render_id': 1})

    file_type = invoice['file_type']
    file_url = render_view(1, '52519517682584b1848886a1d25e4027bda2dc6db9802c35ffc5d81f8a36217d')

    r = requests.get(file_url, allow_redirects=True)
    assert file_url == "https://rendered-invoices.s3.ap-southeast-2.amazonaws.com/invoice1.html"
    open('test1', 'wb').write(r.content)
    assert file_type == (magic.from_file('test1', mime=True).split("/")[1])
    os.remove('test1')
    os.remove('invoice_render.html')

