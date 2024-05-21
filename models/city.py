#!/usr/bin/python3
"""
City class for the AirBnB clone project.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.
    """
    state_id = ""
    name = ""
