# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:30:32 2019

@author: Raymond
"""

"""
Make sure to add new skills to load/save atm
"""
class Player:
    def __init__(self):
        self.level = 0
        #based on DND level system next_lvl = curr_lvl*(curr_lvl-1)*500
        self.level_array = [0, 1000, 3000, 6000, 10000, 15000, 21000, 28000, 36000, 45000, 55000, 66000, 78000, 91000, 105000, 120000, 136000, 153000, 171000, 190000]
        self.health = 100
        self.max_health = 100
        self.exp = 0
        self.gold = 10
        self.max_mana = 100
        self.current_mana = 100
        self.run_percent = .25
        
    
        
        self.is_dead = False
        
        self.player_class = 'none'
        
        self.currently_equipped = []
        self.inventory = []
        self.equipment = []
        
        self.known_skills = []
        
        #get from Dungeon_Skills
        self.unknown_skills = []
        
        #room indicators
        self.ran_away = False
        self.descend = False
        self.burn_bonfire = False
        
        #bonfire skills
        self.fix_amount = 10
        self.rest_heal_amount = 10
        self.overheal_amount = 5
        self.rest_exp_amount = 500
        
        #perm upgrades
        self.perm_upgrades = []
    