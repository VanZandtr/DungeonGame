# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:36:50 2019

@author: Raymond
"""

class Room:
    def __init__(self, room_id, north, south, east, west, room_type):
        self.room_id = room_id
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.room_type = room_type
        