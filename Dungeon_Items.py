# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 21:34:12 2019

@author: Raymond
"""
class Items:
    def __init__(self):
        #temp health/mana is a buffer until used up -> ie damage is taken from temp each round first
        #name 0, type 1, cost 2, damage added 3, addition max health 4, additional max mana 5, armor rating 6, durability 7, additional properties 8, description 9, creation name 10
        self.wooden_shield = ['Wooden Shield', 'hand', 50, 0, 0, 0, 1, 10, 'none', '~ Better than no shield', 'wooden_shield']
        self.rusty_helm = ['Rusty Helmet', 'head', 50, 0, 0, 0, 1, 10, 'none', '~ Ouch Ouch Ouch', 'rusty_helm']
        self.rusty_chest = ['Rusty Chest Plate', 'chest', 50, 0, 0, 0, 1, 10, 'none', '~ Does this even work?', 'rusty_chest']
        self.rusty_legs = ['Rusty Greaves', 'legs', 50, 0, 0, 0, 1, 10, 'none', '~ You feel slower and maybe better protected', 'rusty_legs']
        self.rusty_sword = ['Rusty Sword', 'hand', 50, 3, 0, 0, 0, 10, 'none', '~ This sword has seen better days', 'rusty_sword']
        self.iron_sword = ['Iron Sword', 'hand', 150, 5, 0, 0, 0, 100, 'none', '~ Average sword', 'iron_sword']
        self.kal_thon_sword = ['Kal Thon (Legendary Sword)', 'hand', 10000, 100, 100, 100, 10, 10000, 'none', '~BEHOLD MY MIGHT', 'kal_thon_sword']
        
        #Potions
        #name, type, cost, max health increase, max mana increase, temp health increase, temp mana increase, description
        self.minor_health_potion = ['Minor Health Potion', 'item', 25, 0, 0, 10, 0, '~ Restores 10 points of health']
        self.minor_mana_potion = ['Minor Health Potion', 'item', 25, 0, 0, 0, 15, '~ Restores 15 points of mana']
        self.nic_tha_tal_potion = ['Potion of Nic\'Tha Tal', 'item', 25, 1000, 1000, 0, 0, '~ *whisper* Give me your power and you shall never die *whisper*']
        self.test_potion = ['Test', 'item', 25, 1000, 1000, 1000, 1000, '~ Test']
        
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
        
        self.veryeasy_shop_equipment = [self.rusty_sword, self.rusty_helm, self.rusty_helm, self.rusty_legs, self.rusty_chest]
        
        self.veryeasy_shop_item = [self.minor_health_potion, self.minor_health_potion, self.minor_mana_potion, self.minor_mana_potion, self.nic_tha_tal_potion]
        
    def useItem(self, item, player):
        
        #name, type, cost, max health increase, max mana increase, temp health increase, temp mana increase, description
        
        #max health
        print(item)
        print(item[3])
        if float(item[3]) > 0:
            player.max_health += float(item[3]);
            print("Max Health Increased")
            print(player.max_health)
            
        #max mana
        if float(item[4]) > 0:
            player.max_mana += float(item[4]);
            print("Max Mana Increased")
            print(player.max_mana)
        
        #temp health
        if float(item[5]) > 0:            
            if (player.health + float(item[5])) > player.max_health:
                player.health = player.max_health;
            else:
                player.health += float(item[5])
                
            print("Health Increased")
            print(player.health)
        
        #temp mana
        if float(item[6]) > 0:            
            if (player.current_mana + float(item[6])) > player.max_mana:
                player.current_mana = player.max_mana;
            else:
                player.current_mana += float(item[6])
                
            print("Mana Increased")
            print(player.current_mana)
            
        #------------------------------------------
        #make negative effect potions
        #------------------------------------------
    
        
        player.inventory.remove(item)
             
    