#!/usr/bin/python3
"""  class User that inherits from BaseModel and create a user model"""

from models.base_model import BaseModel


class User(BaseModel):
    """class defining user using various attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""