#!/usr/bin/python3
""" class model Review that inherit from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Model Review that inherit from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""