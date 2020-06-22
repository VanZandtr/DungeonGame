# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 21:09:45 2020

@author: rvanza632
"""

import pickle as pickle


class Perm_Upgrade:
    def __init__(self):
        #key, name, description, cost(gold)
        self.mana_tree = [["M20","Minor Mana Increase", "Increase Mana by 20", 100], ["SR1", "Skill Cost Reduction", "Decrease ALL Spells Mana Cost by 1", 5000]]
        
        self.health_tree = [["H20","Minor Health Increase", "Increase Health by 20", 100], ["DR1", "Damage Reduction", "Decrease ALL by 1", 5000]]
    
    def load_upgrades(self, player):
        with open("perm_upgrades.txt", "rb") as lf:
            player.perm_upgrades = pickle.load(lf)
            print(player.perm_upgrades)
        lf.close()
        
    def save_upgrades(self, player):
        #add saves for trees, that way we can delete upgrades already bought
        with open("perm_upgrades.txt", "ab") as save_file:
            #clear file
            save_file.seek(0)
            save_file.truncate()
            #player data
            print(player.perm_upgrades)
            pickle.dump(player.perm_upgrades, save_file)
        save_file.close
        
    def perm_key_applicator(self, list_of_upgrades):
        print("get Keys and apply effects")