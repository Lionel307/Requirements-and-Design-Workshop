import pytest
from src.render import render_html
from src.database import clear_users, clear_invoices, clear_bucket, access_db
from src.errors import InputError, XMLError

@pytest.fixture
def clear_data():
    clear_invoices()
    clear_bucket()

def test_empty_api_key(clear_data):
    with pytest.raises(InputError):
        render_html("tests/valid_sample.xml", '')

def test_return_info(clear_data):
    ret = render_html("tests/valid_sample.xml", "api_key")
    assert ret == {
        'url': 'https://rendered-invoices.s3.ap-southeast-2.amazonaws.com/invoice1.html',
        'render_id': 1,
    }
    ret = render_html("tests/valid_sample.xml", "api_key2")
    assert ret == {
        'url': 'https://rendered-invoices.s3.ap-southeast-2.amazonaws.com/invoice2.html',
        'render_id': 2,
    }
    ret = render_html("tests/valid_sample.xml", "api_key3")
    assert ret == {
        'url': 'https://rendered-invoices.s3.ap-southeast-2.amazonaws.com/invoice3.html',
        'render_id': 3,
    }

def test_storage(clear_data):
    render_html("tests/valid_sample.xml", "api_key")
    collection = access_db()
    invoice = collection.find_one({'render_id': 1})

    assert invoice['render_id'] == 1
    assert invoice['file_type'] == 'html'
    assert invoice['file_url'] == 'https://rendered-invoices.s3.ap-southeast-2.amazonaws.com/invoice1.html'
    assert invoice['api_key'] == 'api_key'

def test_invalid_xml(clear_data):
    with pytest.raises(XMLError):
        render_html("tests/invalid_sample.xml", "api_key")
