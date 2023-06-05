#!/usr/bin/python3
'''User model'''

from models.base_model import BaseModel


class User(BaseModel):
    '''defines a user and all their attributes'''

    email = ''
    password = ''
    first_name = ''
    last_name = ''
