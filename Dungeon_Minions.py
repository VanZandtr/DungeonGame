# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 20:37:47 2019

@author: Raymond
"""

import random
import math
from Dungeon_Skills import Skills
from Dungeon_Items import Items

class Minions:
    def __init__(self, minion_id, player):
        self.minion_id = minion_id
        self.player = player
        
        #name,health,attack_type,attack_strength,quantity,damage,attack miss chance, power name, power damage, power chance
        self.bosses = [['big_rat', 100, 'beast', 'easy', 1, [5,6], .1, 'roar', 10, .2], ['theif_boss', 50, 'human', 'medium', 1, [5,6,7], .1, 'assinate', 20, .15]]
        
        #name,health,attack_type,attack_strength,quantity,damage, attack miss chance
        self.minions = [['rat', 10, 'beast', 'very easy', 3, [1,2], .25], ['thief', 5, 'human','very easy', 4, [1,2,3], .2]]
        
        
        
    def spawnMinion(self):
        minion_id = self.minion_id
        print("event:", minion_id)
        
        self.createMinionEncounter(minion_id)
        

    def spawnBoss(self):
        boss_id = self.minion_id
        print("event:", boss_id)
        
        self.createBossEncounter(boss_id)
        
    def give_minion_reward(self,minion_difficulty, minion_quantity):
        equipment_chance = random.uniform(0,1)
        item_chance = random.uniform(0,1)
        exp_output = random.uniform(10,15)
        gold_output = random.uniform(1,5)
        gold_output = math.floor(gold_output)
        exp_output = math.floor(exp_output)
        
        item_Class = Items()
        
        if minion_difficulty in ['very easy']:
            gold_output = gold_output
            exp_output = exp_output
            
            if item_chance > .9:
                new_item = random.choice(item_Class.veryeasy_item)
                print('Found:',new_item)
                self.player.inventory.append(new_item.copy())
                
            if equipment_chance > .9:
                new_equipment = random.choice(item_Class.veryeasy_equipment)
                print('Found:', new_equipment)
                self.player.equipment.append(new_equipment.copy())
                  
        elif minion_difficulty is 'easy':
            gold_output = math.floor(0.5*gold_output) + gold_output
            exp_output = math.floor(0.5*exp_output) + exp_output
            
            if item_chance > .8:
                new_item = random.choice(item_Class.easy_item)
                print('Found:',new_item)
                self.player.inventory.append(new_item.copy)
                
            if equipment_chance > .8:
                new_equipment = random.choice(item_Class.easy_equipment)
                print('Found:', new_equipment)
                self.player.equipment.append(new_equipment.copy())
            
        elif minion_difficulty is 'medium':
            gold_output = 2*gold_output
            exp_output = 2*exp_output
            
            if item_chance > .6:
                new_item = random.choice(item_Class.medium_item)
                print('Found:',new_item)
                self.player.inventory.append(new_item.copy())
                
            if equipment_chance > .6:
                new_equipment = random.choice(item_Class.medium_equipment)
                print('Found:', new_equipment)
                self.player.equipment.append(new_equipment.copy())
            
        elif minion_difficulty is 'hard':
            gold_output = math.floor(4*gold_output) + gold_output
            exp_output = math.floor(4*exp_output) + exp_output
            
            if item_chance > .4:
                new_item = random.choice(item_Class.hard_item)
                print('Found:',new_item)
                self.player.inventory.append(new_item.copy())
                
            if equipment_chance > .4:
                new_equipment = random.choice(item_Class.hard_equipment)
                print('Found:', new_equipment)
                self.player.equipment.append(new_equipment.copy())
            
        elif minion_difficulty is 'very hard':
            gold_output = 7*gold_output
            exp_output = 7*exp_output
            
            if item_chance > .2:
                new_item = random.choice(item_Class.veryhard_item)
                print('Found:',new_item)
                self.player.inventory.append(new_item.copy())
                
            if equipment_chance > .2:
                new_equipment = random.choice(item_Class.veryhard_equipment)
                print('Found:', new_equipment)
                self.player.equipment.append(new_equipment.copy())
            
        else:
            gold_output = 10*gold_output
            exp_output = 10*exp_output
            
            if item_chance > 0:
                new_item = random.choice(item_Class.impossible_item)
                print('Found:',new_item)
                self.player.inventory.append(new_item.copy())
                
            if equipment_chance > 0:
                new_equipment = random.choice(item_Class.impossible_equipment)
                print('Found:', new_equipment)
                self.player.equipment.append(new_equipment.copy())

        for minion in range(minion_quantity):
            gold_output+=gold_output
            exp_output+=exp_output
        
        self.player.gold += gold_output
        self.player.exp += exp_output
        
        print()
        print('Gold Reward:', gold_output)
        print('Exp Reward:', exp_output)
        print('Total Gold:', self.player.gold)
        print('Total Exp:', self.player.exp)
        print()
        
        
            
    def createMinionEncounter(self, minion_id):
        minion = []
                
        for new_minion in self.minions:
            if minion_id is new_minion[0]:
                print("Watch out adventurer!")
                minion = new_minion
                    
        if minion == '':
            print('Could not find a valid minion')
                    
                    
        health = minion[1]
        minion_difficulty = minion[3]
        minion_quantity = minion[4]
        minion_damage = minion[5]
        minion_miss_chance = minion[6]
        
        minions_display = []
        
        for new_minion in range(minion_quantity):
            minions_display.append([minion_id, health, minion_damage])
            
        while(True):
            print()
            print(minions_display, end = " ")
            
            turn_not_over = True
            while(turn_not_over):
                
                if minion_quantity != 1:
                    display_number = []
                    counter = 1
                    for minion_number in range(minion_quantity):
                        display_number.append(counter)
                        counter +=1
                        
                print()
                battle_text = 'What would the adventurer like to do?' + '\n' + '\n' + 'Attack' + '\n' + 'Use Skill' + '\n' + 'Use Item' + '\n' + 'Run'  + '\n' + '\n' + '>'
                command = input(battle_text)
                
                if command in ['a','A','attack', 'Attack']:
                    
                    damage = 0
                    weapon = None
                    
                    #get damage number
                    hands_counter = 0
                    for e in self.player.currently_equipped:
                        if e[1] == 'hand':
                            hands_counter +=1;
                            
                    if hands_counter == 0:    
                        damage = math.ceil(random.uniform(1,4))
                        
                    elif hands_counter == 1:
                        for e in self.player.currently_equipped:
                            if e[1] == 'hand':
                                damage = e[3]
                                weapon = e
                    else:
                        weapon_selected = False
                        while(True):
                            if weapon_selected is True:
                                break
                            
                            for e in self.player.currently_equipped:
                                if e[1] == 'hand':
                                    print(e)

                            weapon_select = input('What weapon would the adventurer like to use?>')
                            for e in self.player.currently_equipped:
                                if weapon_select == e[0]:
                                    damage = e[3]
                                    weapon = e
                                    weapon_selected = True
                                    break
                                else:
                                    print("The adventurer does not have that weapon")
                                    break

                    
                    if minion_quantity != 1:
                        print('Which will the adventurer attack?')
                        print()
                        for x in display_number:
                            if minions_display[x-1][1] is not 0:
                                print(x)
                        print()
                        
                        minion_number_str = input('>')
                        try:
                            minion_number = int(minion_number_str)
                        except:
                            print('The adventure needs to select a valid enemy')
                            turn_not_over = True
                            
                        print()
                        
                        if minion_number in display_number and minions_display[minion_number-1][1] is not 0 :
                            print('The adventurer did',damage,'damage')
                            #deal damage to that minion
                            if damage >= minions_display[minion_number-1][1]:
                                print(minions_display[minion_number-1][0],'has died')
                                minions_display[minion_number-1][1] = 0
                                display_number.remove(minion_number)
                                
                            else:
                                print(minions_display[minion_number-1][0],'has taken',damage,'damage')
                                minions_display[minion_number-1][1] -= damage
                                                            
                            damage_to_weapon_chance = math.ceil(random.uniform(1,4))
                            #if damage_to_weapon_chance == 4:
                            if damage_to_weapon_chance > 0:
                                damage_to_weapon = math.ceil(random.uniform(1, float(weapon[7])/4))
                                print('The adventurer\'s ',e[0],' sustained ',damage_to_weapon,' damage')
                                e[7] = float(weapon[7]) - damage_to_weapon
                                if e[7] <= 0:
                                    print('The adventurer\'s',e[0], 'was destroyed')
                                    self.player.currently_equipped.remove(e)
                                
                                
                            turn_not_over = False
                            
                            
                            
                        elif minion_number in display_number and minions_display[minion_number-1][1] is 0 :
                            print('The adventure has already killed this enemy')
                            turn_not_over = True
                        else:
                            print('The adventure needs to select a valid enemy')
                            turn_not_over = True
                    else:
                        print('The adventurer did',damage,'damage')
                        #deal damage to that minion
                        if damage >= minions_display[0][1]:
                            print(minions_display[0][0],'has died')
                            minions_display[0][1] = 0
                        else:
                            print(minions_display[0][0],'has taken',damage,'damage')
                            minions_display[0][1] -= damage
                        turn_not_over = False
                        
                    
                elif command in ['s','S','skill', 'Skill', 'use Skill', 'use skill', 'Use Skill', 'Use skill']:
                    
                    if len(self.player.known_skills) == 0:
                        print('The adventurer knows no skills')
                        turn_not_over = True
                        
                    elif self.player.current_mana == 0:
                        print('The adventurer has no mana')
                        turn_not_over = True
                        
                    else:
                        print('What skill will the adventurer use?')
                        print()
                        print('Mana:',self.player.current_mana)
                        print('Skill','Mana Cost','Damage')
                        for skill in range(len(self.player.known_skills)):
                            damage = str(self.player.known_skills[skill][3]) + '-' + str(self.player.known_skills[skill][4])
                            print(self.player.known_skills[skill][0],self.player.known_skills[skill][2], damage)
                        
                        skill_command = input('>')
                        skill_found = False
                        for skill in range(len(self.player.known_skills)):
                            if skill_command == self.player.known_skills[skill][0]:
                                skill_found = True
                                cast_skill = self.player.known_skills[skill]
                                
                                if cast_skill[2] > self.player.current_mana:
                                    print('The adventurer does not have enough mana to cast this spell')
                                    print()
                                    turn_not_over = True
                                    
                                
                                print('The adventurer casts a skill')
                                print()
                                no_attack_flag = False
                                no_end_turn_flag = False
                                
                                if cast_skill[6] == 'Single':
                                    if minion_quantity != 1:
                                        print('Which will the adventurer cast', cast_skill[0],'on?')
                                        print()
                                        for x in display_number:
                                            if minions_display[x-1][1] is not 0:
                                                print(x)
                                        print()
                                        
                                        minion_number_str = input('>')
                                        try:
                                            minion_number = int(minion_number_str)
                                        except:
                                            print('The adventure needs to select a valid enemy')
                                            turn_not_over = True
                                            
                                        print()
                                        
                                        if minion_number in display_number and minions_display[minion_number-1][1] is not 0 :
                                            new_skill = Skills()
                                            #get damage number
                                            special_text = new_skill.castSingleTargetSpell(cast_skill, minion, minions_display,minion_number,display_number, self.player)
                                            
                                            for flag in special_text:
                                                if flag == 'no_attack':
                                                    no_attack_flag = True
                                                    
                                                elif flag == 'no_turn_end':
                                                    no_end_turn_flag = True
                                                
                                            if no_attack_flag is True:
                                                minions_display[minion_number-1][2] = 0

                                            if no_end_turn_flag is True:    
                                                turn_not_over = True
                                                
                                            else:
                                                turn_not_over = False
                                            
                                            
                                        elif minion_number in display_number and minions_display[minion_number-1][1] is 0 :
                                            print('The adventure has already killed this enemy')
                                            print()
                                            turn_not_over = True
                                        else:
                                            print('The adventure needs to select a valid enemy')
                                            print()
                                            turn_not_over = True
                                else:
                                    new_skill = Skills()
                                            
                                    special_text = new_skill.castAOESpell(cast_skill, minion, minions_display, display_number, self.player)
                                    
                                    for flag in special_text:
                                        if flag == 'no_attack':
                                            no_attack_flag = True
                                            
                                        elif flag == 'no_turn_end':
                                            no_end_turn_flag = True
                                        
                                    if no_attack_flag is True:
                                        minions_display[minion_number-1][2] = 0

                                    if no_end_turn_flag is True:    
                                        turn_not_over = True
                                        
                                    else:
                                        turn_not_over = False
                                    
                        if skill_found == False:    
                            print('That is not a skill the adventurer knows')
                            turn_not_over = True

                    
                elif command in ['i','I','item', 'Item', 'use Item', 'use item', 'Use Item', 'Use item']:
                    if len(self.player.inventory) is 0:
                        print("The adventurer has nothing to use")
                        turn_not_over = True
                        
                        
                    for item in self.player.inventory:
                            print(item[0], item[7]);
                        
                    item_command = input('Which item would the adventurer like to use?>')
                    item_found = False
                    for item in self.player.inventory:
                        if item_command == item[0]:
                            item_found = True
                            
                            new_item = Items();
                            #use the item
                            new_item.useItem(item, self.player);
                            print('item removed')
                            print()
                            
                    if item_found == True:
                        turn_not_over = False
                    else:
                        turn_not_over = True
                    
                elif command in ['r','R','run', 'Run']:
                    run = random.uniform(0,1)
                    if run <= self.player.run_percent:
                        print('The adventurer runs away')
                        print()
                        self.player.ran_away = True
                        return
                    else:
                        print('The adventurer cannot run away')
                        print()
                        turn_not_over = False
                     
            #minions attack
            print()
            for new_minion in minions_display:
                if new_minion[1] is not 0:
                    hit = random.random()
                    if new_minion[2] == 0 or hit < minion_miss_chance:
                        print(minion[0], 'missed')
                        #reset damage if silenced
                        new_minion[2] = minion_damage
                        
                    else:
                        damage = random.choice(minion_damage)
                        print(minion[0],'hit for', damage)
                        
                        armor_modifier = 0
                        armor_rating = 0
                        for armor in self.player.currently_equipped:
                            if armor[1] is not 'hand':
                                armor_modifier += 1
                                armor_rating += float(armor[6])
                                
                                #calulcate damage to armors
                                damage_to_armor_chance = math.ceil(random.uniform(1,4))
                                #if damage_to_weapon_chance == 4:
                                if damage_to_armor_chance > 0:
                                    damage_to_armor = math.ceil(random.uniform(1, armor[6]/4))
                                    print('The adventurer\'s ',armor[0],' sustained ',damage_to_armor,' damage.')
                                    armor[7] = float(armor[7]) - damage_to_armor
                                    if armor[7] <= 0:
                                        print('The adventurer\'s',armor[0], 'was destroyed.')
                                        self.player.currently_equipped.remove(e)
                    
                        armor_absorption = armor_modifier * armor_rating * self.player.level
                        
                        if damage - armor_absorption <= 0:
                            print("The adverturer\'s armor absorbed the blow.")
                            damage = 0
                        else:
                            print("The adventurer sustained ", damage," damage.")
                            damage -= armor_absorption
                        
                        self.player.health -= damage
                        
                        
                        
            print()
            
            if self.player.health <= 0:
                self.player.is_dead = True
                return
                    
            print('Health', self.player.health)
            print()
        
            
            #test ----- INSTA KILL ENEMIES
            '''
            print('AUTO KILLED ALL ENEMIES')
            for new_minion in minions_display:
                new_minion[1] = 0
            '''
            
                
            #check if all minions are dead    
            death_counter = 0
            for new_minion in minions_display:
                if new_minion[1] is 0:
                    death_counter +=1
                if death_counter is minion_quantity:
                    self.give_minion_reward(minion_difficulty, minion_quantity)
                    return


    def createBossEncounter(self, minion_id):
        for boss in self.bosses:
            if minion_id is self.bosses[0]:
                print("Oh no adventurer. It comes.")
            else:
                print("could not find that boss")