import pytest
from src.auth import auth_register, auth_login
from src.database import clear_users, access_users
from src.errors import InputError, AccessError

@pytest.fixture
def register_users():
    clear_users()
    auth_register("Bob", "myemail1@gmail.com", "password1", 'business')
    auth_register("Jake", "myemail2@gmail.com", "password2", 'business')
    auth_register("Tom", "myemail3@gmail.com", "password3", 'business')

# Test successful logins returns correct api keys
def test_return_api_key(register_users):
    assert auth_login("myemail1@gmail.com", "password1") == 'bbbf58666765322aa32295bc21498647485d528a590c40cffafe8b61bf0d6865'
    assert auth_login("myemail2@gmail.com", "password2") == 'd4cf90a978926ec809fcc718f6369a1d6f124aa1f25fd15612239aceb9721b23'
    assert auth_login("myemail3@gmail.com", "password3") == 'c79e534d438993453a01821e9bf049f6313cbc9bd86bd4e5df7e76dc4b597597'

# Test if email inputted is not a correct email (format wise) returns InputError
def test_email_invalid(register_users):
    with pytest.raises(InputError):
        auth_login("myemail", "password")

    with pytest.raises(InputError):
        auth_login("@mail.com", "password")

    with pytest.raises(InputError):
        auth_login("", "password")

    with pytest.raises(InputError):
        auth_login("", "")

# Test if email does not exist/not registered returns InputError
def test_email_not_exist(register_users):
    with pytest.raises(InputError):
        auth_login("fake@gmail.com", "password123")

    with pytest.raises(InputError):
        auth_login("myemail@gmail.com", "password1")

# Test if password is empty returns InputError
def test_password_not_empty(register_users):
    with pytest.raises(InputError):
        auth_login("myemail@gmail.com", "")

    with pytest.raises(InputError):
        auth_login("myemail1@gmail.com", "")

# Test if password is incorrect for valid email returns AccessError
def test_user_storage(register_users):
    with pytest.raises(AccessError):
        auth_login("myemail1@gmail.com", "incorrectPass")

    with pytest.raises(AccessError):
        auth_login("myemail2@gmail.com", "password1")
