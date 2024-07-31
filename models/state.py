#!/usr/bin/python3
""" model State that inherit from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """inherit from BaseModel and collect the name of the state"""
    name = ""