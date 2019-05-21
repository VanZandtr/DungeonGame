# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:31:53 2019

@author: Raymond
"""

import random
import math

class Skills:
    def __init__(self):

        #name, spell level, mana cost, damage min, damage max, damage type, spell type(AOE, Single Target, ...), enemy types effected, Special Spell text, Spell Desc
        self.wizard_skills = [['Firebolt', 1, 10, 10, 15, 'fire', 'Single', 'All', 'none', 'A well known wizard cantrip'], ['Fireball', 4, 35, 50, 60, 'fire', 'AOE', 'All', 'none', 'Hurl a massive ball of fire']]
        
        self.priest_skills = [['Silence', 1, 10, 0, 0, 'holy', 'Single', 'All', ['no_attack', 'no_turn_end'], 'Stop a single enemy from attacking. This action does not end the turn'], ['Turn Undead', 4, 35, 100, 100, 'holy', 'AOE', 'undead', 'none', 'Deal massive damage to undead enemies']]
        
        
    def castSingleTargetSpell(self, skill, minion, minions_display, minion_number, display_number, player):
        if skill[7] == minion[2] or skill[7] == 'All':
            if skill[3] != 0 and skill[4] != 0:
                
                damage = math.ceil(random.uniform(skill[3], skill[4]))
                
                #deal damage to that minion
                if damage >= minions_display[minion_number-1][1]:
                    print(minions_display[minion_number-1][0],'has died')
                    minions_display[minion_number-1][1] = 0
                    display_number.remove(minion_number)
                    
                    
                else:
                    print(minions_display[minion_number-1][0],'has taken',damage,'damage')
                    minions_display[minion_number-1][1] -= damage
                    
            
            player.current_mana -= skill[2]
            
            if player.current_mana < 0:
                player.current_mana = 0
            
            print('Mana', player.current_mana)
            return skill[8]
        
        else:
            print('Adventurer that minion was unaffected by',skill[0],'!')
            return []
        
    
    def castAOESpell(self, skill, minion, minions_display, display_number, player):
        if skill[7] == minion[2] or skill[7] == 'All':
            if skill[3] != 0 and skill[4] != 0:
                
                damage = math.ceil(random.uniform(skill[3], skill[4]))
                
                #deal damage to all minions
                counter = 0
                for current_minion in minions_display:
                    if damage >= current_minion[1]:
                        print(current_minion[0],'has died')
                        current_minion[1] = 0
                        display_number.remove(counter+1)
                    
                    else:
                        print(current_minion[0],'has taken',damage,'damage')
                        current_minion[1] -= damage
                    counter+=1
                    
            
            player.current_mana -= skill[2]
            
            if player.current_mana < 0:
                player.current_mana = 0
                
            print()
            print('Mana', player.current_mana)
            return skill[8]
        
        else:
            print('Adventurer the minions seem unaffected by',skill[0],'!')
            return []
        
    def getSkills(self,player, _class):
        
        class_string = str(_class)
        
        player.player_class = _class
        
        if class_string in ['Wizard']:
            player.unknown_skills = self.wizard_skills
        elif class_string in ['Priest']:
            player.unknown_skills = self.priest_skills
        else:
            print('Error getting class')
            
        