# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:30:32 2019

@author: Raymond
"""

class Player:
    def __init__(self):
        self.level = 0
        self.level_array = [0,1000,2000,3000,4000]
        self.health = 100
        self.max_health = 100
        self.exp = 0
        self.gold = 10
        self.max_mana = 100
        self.current_mana = 100
        self.run_percent = .25
        self.ran_away = False
        self.weapon_equipped = 'none'
        
        self.is_dead = False
        
        self.player_class = 'none'
        
        self.inventory = []
        self.equipment = []
        
        self.known_skills = []
        
        #get from Dungeon_Skills
        self.unknown_skills = []
    