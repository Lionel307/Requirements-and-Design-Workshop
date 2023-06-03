import pytest
import boto3
from src.database import clear_users, clear_invoices, clear_bucket, access_db, render_delete, \
                        ACCESS_KEY, SECRET_KEY
from src.auth import auth_register
from src.errors import InputError, AccessError
from src.render import render_html

@pytest.fixture
def clear_data():
    clear_invoices()
    clear_bucket()
    clear_users()

@pytest.fixture
def register(clear_data):
    # Register 2 users
    key1 = auth_register('Bob', 'myemail1@gmail.com', 'password', 'business')
    key2 = auth_register('Jake', 'myemail2@gmail.com', 'password2', 'business')

    # Each user renders an invoice
    render_html("tests/valid_sample.xml", key1)
    render_html("tests/valid_sample.xml", key2)

    return [key1, key2]

def test_empty_api_key(clear_data):
    with pytest.raises(InputError):
        render_delete(1, '')

def test_invalid_api_key(register):
    with pytest.raises(AccessError):
        render_delete(2, register[0])

    with pytest.raises(AccessError):
        render_delete(1, register[1])

def test_storage(register):
    render_delete(1, register[0])
    render_delete(2, register[1])

    # Check if mongoDB invoice collection is empty
    collection = access_db()
    results = list(collection.find())
    assert len(results) == 0

    # Check if S3 bucket is empty
    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    bucket = s3.Bucket('rendered-invoices')
    count = bucket.objects.filter()
    assert len(list(count)) == 0
