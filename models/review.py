#!/usr/bin/python3
'''Review model'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''defines a review and all its attributes'''

    place_id = ''
    user_id = ''
    text = ''
