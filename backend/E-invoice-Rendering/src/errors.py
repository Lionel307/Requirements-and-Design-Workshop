'''this module contains classes for the errors'''
from werkzeug.exceptions import HTTPException

class AccessError(HTTPException):
    '''Class for Acces error'''
    code = 403
    message = 'No message specified'

class InputError(HTTPException):
    '''Class for Input error'''
    code = 400
    message = 'No message specified'

class XMLError(HTTPException):
    '''Class for XML error'''
    code = 276
    message = 'No message specified'
