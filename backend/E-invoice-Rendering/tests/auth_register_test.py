import pytest
from src.auth import auth_register
from src.database import clear_users, access_users
from src.errors import InputError

@pytest.fixture
def clear_data():
    clear_users()

def test_return_api_key(clear_data):
    assert auth_register("Bob","myemail@gmail.com", "password", 'business') == '52519517682584b1848886a1d25e4027bda2dc6db9802c35ffc5d81f8a36217d'

def test_email_invalid(clear_data):
    with pytest.raises(InputError):
        auth_register("Bob","myemail", "password", 'business')

    with pytest.raises(InputError):
        auth_register("Bob","@mail.com", "password", 'business')

def test_email_used(clear_data):
    auth_register("Bob", "myemail@gmail.com", "password", 'business')
    with pytest.raises(InputError):
        auth_register("Bob", "myemail@gmail.com", "password123", 'business')

def test_name_used(clear_data):
    auth_register("Bob", "myemail@gmail.com", "password", 'individual')
    with pytest.raises(InputError):
        auth_register("Bob", "myemail2@gmail.com", "password123", 'individual')

def test_acc_type_invalid(clear_data):
    with pytest.raises(InputError):
        auth_register("Bob", "myemail2@gmail.com", "password123", 'professional')

def test_name_empty(clear_data):
    with pytest.raises(InputError):
        auth_register("", "myemail2@gmail.com", "password123", 'business')

def test_password_length(clear_data):
    with pytest.raises(InputError):
        auth_register("Bob", "myemail@gmail.com", "pass", 'business')

def test_user_storage(clear_data):
    auth_register("Bob", "myemail@gmail.com", "password", 'business')

    collection = access_users()
    user = collection.find_one({'email': "myemail@gmail.com"})
    encrypted_pass = user['password']
    email = user['email']
    name = user['name']
    account_type = user['account']
    assert name == 'Bob'
    assert email == "myemail@gmail.com"
    assert encrypted_pass == '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
    assert account_type == 'business'