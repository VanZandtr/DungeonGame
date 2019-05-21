# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 21:34:12 2019

@author: Raymond
"""
class Items:
    def __init__(self):
        #name, cost, damage added, addition max health, additional max mana, mana restore, health restore, additional properties, description
        self.rusty_sword = ['Rusty Sword', 50, 3, 0, 0, 0, 0, 'none', '~ This sword has seen better days']
        self.iron_sword = ['Iron Sword', 150, 5, 0, 0, 0, 0, 'none', '~ Average sword']
        self.kal_thon_sword = ['Kal Thon (Legendary Sword)', 10000, 100, 100, 100, 100, 100, 'none', '~BEHOLD MY MIGHT']
        
        #Potions
        #name, cost, max health increase, max mana increase, temp health increase, temp mana increase, description
        self.minor_health_potion = ['Minor Health Potion', 25, 0, 0, 10, 0, '~ Restores 10 points of health']
        self.minor_mana_potion = ['Minor Health Potion', 25, 0, 0, 0, 15, '~ Restores 15 points of mana']
        self.nic_tha_tal_potion = ['Potion of Nic\'Tha Tal', 25, 1000, -1000, 0, 0, '~ *whisper* Give me your power and you shall never die *whisper*']
        
        self.veryeasy_equipment = ['rusty sword']
        self.easy_equipment = ['rusty sword']
        self.medium_equipment = ['rusty sword']
        self.hard_equipment = ['rusty sword']
        self.veryhard_equipment = ['rusty sword']
        self.impossible_equipment = ['rusty sword']
        
        self.veryeasy_item = ['minor_health_potion']
        self.easy_item = ['minor_health_potion']
        self.medium_item = ['minor_health_potion']
        self.hard_item = ['minor_health_potion']
        self.veryhard_item = ['minor_health_potion']
        self.impossible_item = ['minor_health_potion']
        
        self.veryeasy_shop_equipment = [self.rusty_sword,self.rusty_sword, self.rusty_sword, self.iron_sword, self.kal_thon_sword]
        
        self.veryeasy_shop_item = [self.minor_health_potion, self.minor_health_potion, self.minor_mana_potion, self.minor_mana_potion, self.nic_tha_tal_potion]