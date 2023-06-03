'''this module contains functions for authorisation'''
import hashlib
import re
from datetime import datetime
from src.errors import InputError, AccessError
from src.database import access_users, api_key_check
from src.track import log

def auth_register(name, email, password, account_type):
    """
    Registers a new user given their email and password.
    Returns their personal API key that enables them to use the other routes.

    Arguments:
        email: str
        password: str

    Exceptions:
        InputError when any of:
            - Email is not a valid email

    Return Value:
        api_key: str
    """
    start_time = datetime.now()

    # Check if name is already registered
    if name_exists(name):
        log("/auth/register", start_time, 400)
        raise InputError("Name has already been registered.")
    
    # Check if name is empty
    if name == '':
        log("/auth/register", start_time, 400)
        raise InputError("Please enter a name.")
    
    # Check if email is valid
    if email_invalid(email):
        log("/auth/register", start_time, 400)
        raise InputError("Email is not valid.")

    # Check if email is already registered
    if email_exists(email):
        log("/auth/register", start_time, 400)
        raise InputError("Email has already been registered.")

    # Check if password is not empty
    if len(password) < 5:
        log("/auth/register", start_time, 400)
        raise InputError("Password must have at least 5 characters")

    if account_type != 'business' and account_type != 'individual':
        log("/auth/register", start_time, 400)
        raise InputError("Account type must be either business or individual")

    # Encrypt given password
    encrypted_pass = hashlib.sha256(password.encode()).hexdigest()

    # Access user database
    collection = access_users()

    # Stores the user's email and encrypted password into the database
    collection.insert_one({"name": name, "email": email, 'password': encrypted_pass, 'account': str(account_type)})

    # Generate API Key by hashing the combination of user's email and encrypted password
    combine = email + encrypted_pass
    api_key = hashlib.sha256(combine.encode()).hexdigest()
    return api_key

def auth_login(email, password):
    """
    Logins a new user given their email and password.
    Returns their personal API key that enables them to use the other routes.

    Arguments:
        email: str
        password: str

    Exceptions:
        InputError when any of:
            - Email is not a valid email
            - Email does not exist
            - Password is empty string
        AccessError when any of:
            - Password is incorrect for given valid email

    Return Value:
        api_key: str
    """
    start_time = datetime.now()
    # Check if email is valid
    if email_invalid(email):
        log("/auth/register", start_time, 400)
        raise InputError("Email is not valid.")

    # Check if email is already registered
    if not email_exists(email):
        log("/auth/register", start_time, 400)
        raise InputError("Email does not exist.")

    # Check if password is not empty
    if len(password) == 0:
        log("/auth/register", start_time, 400)
        raise InputError("Please enter your password")

    # Encrypt given password
    encrypted_pass = hashlib.sha256(password.encode()).hexdigest()

    # Generate API Key by hashing the combination of user's email and encrypted password
    combine = email + encrypted_pass
    api_key = hashlib.sha256(combine.encode()).hexdigest()

    # If API key exists in database of users, return API key to user
    if api_key_check(api_key):
        return api_key
    else:
        # Else, AccessError (password incorrect)
        raise AccessError("Password is incorrect.")

def email_exists(email):
    """
    Returns TRUE if email is already registered into the database, FALSE if not.

    Arguments:
        email: str

    Return Value:
        True or False
    """
    # Access user database
    collection = access_users()

    result = collection.find_one({'email': email})
    if result is not None:
        return True
    return False

def name_exists(name):
    """
    Returns TRUE if name is already registered into the database, FALSE if not.

    Arguments:
        name: str

    Return Value:
        True or False
    """
    # Access user database
    collection = access_users()

    result = collection.find_one({'name': name})
    if result is not None:
        return True
    return False

def email_invalid(email):
    """
    Returns TRUE if email is invalid, FALSE if not.

    Arguments:
        email: str

    Return Value:
        True or False
    """
    mail_regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
    # If email matches criteria, then return FALSE, else TRUE
    if re.fullmatch(mail_regex, email):
        return False
    return True
