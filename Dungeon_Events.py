# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 20:38:30 2019

@author: Raymond
"""
from Dungeon_Items import Items
from Dungeon_Minions import Minions
import random


class Event:
    def __init__(self, event_id, player):
        self.event_id = event_id
        #self.success = False
        self.player = player
        
    def fetchEvent(self):
        minions = Minions(self.player)
        while(True):            
            if self.event_id == 'event_enemy_encounter':
                random_minion = random.choice(minions.minions)
                return minions.spawnMinion(random_minion[0])
                break
                
            elif self.event_id == 'event_enemy_encounter_boss':
                random_boss = random.choice(minions.bosses)
                return minions.spawnBoss(random_boss[0])
                    
                break
                
            elif self.event_id == 'event_shop':
                item_Class = Items()
                print("There is a shop here.")
                print()
                
                scripted_phrases = ['LOOK! NO TOUCH! Unless you have coin....', 'WHO BE SNOOPI-. Oh Hello!', '*Rumaging* Take a look, but NO TOUCH! no touch.']
                phrase = random.choice(scripted_phrases)
                print (phrase)
                print()
                print("----------Shop----------")
                
                
                equipment_arr = random.sample(item_Class.veryeasy_shop_equipment, 5)
                item_arr = random.sample(item_Class.veryeasy_shop_item, 5)
                while(True):                
                    print()
                    print('Equipment [name, type, cost, damage added, addition max health, additional max mana, mana restore, armor rating (10), durability, additional properties, description]:')
                    for e in equipment_arr:
                        item_Class.Equipment_Printout(e)
                    print()
                    print('Items [name, type, cost, max health increase, max mana increase, temp health increase, temp mana increase, description]:')
                    for i in item_arr:
                        item_Class.Item_Printout(i)
                    print()
                    
                    item_not_found = True
                    not_enough_gold = False
                    print("----------Shop----------")
                    print()
                    print('Gold:',self.player.gold)
                    print()
                    print('(q, Q, exit, Exit, Quit, quit) to leave.')
                    command = input('What would the adventurer like to purchase?>')
                    if command in ['q','Q','exit','Exit','Quit','quit']:
                        print ("Goodbye")
                        print()
                        break
                    else:
                        for e in equipment_arr:
                            if command == e[0]:
                                if e[2] > self.player.gold:
                                    print('NO GOLD! NO TOUCH!')
                                    not_enough_gold = True
                                    break
                                else:
                                    item_not_found = False
                                    self.player.gold -= e[2]
                                    equipment_arr.remove(e)
                                    self.player.equipment.append(e.copy())
                                    print('A fine purchase.')
                                    break
                            
                        for i in item_arr:
                            if command == i[0]:
                                if i[2] > self.player.gold:
                                    print('NO GOLD! NO TOUCH!')
                                    not_enough_gold = True
                                    break
                                else:
                                    item_not_found = False
                                    self.player.gold -= i[2]
                                    item_arr.remove(i)
                                    self.player.inventory.append(i.copy())
                                    print('A fine purchase.')
                                    break
                        if item_not_found == True and not_enough_gold == False:
                            print('WHAT!')
                            continue
                break                                
                
            elif self.event_id == 'event_bonfire':
                sit_flag = input("A bonfire smolders gentle before the Adventurer. Will the Adventurer rest? (Y/N)>")
                if sit_flag in ['y','Y','Yes','yes']:
                    print('The Adventurer sits.')
                    self.player.burn_bonfire = True
                    
                    print("What would the adventurer like to do?")
                    print()
                    print("Sleep    Current HP: ", self.player.health)
                    print("Repair Equipment")
                    print("Mediate  Current EXP: ", self.player.exp)
                    print()
                    
                    while(True):
                        sit_command = input(">")
                        if sit_command in ['sleep','Sleep','s','S']:
                            if self.player.health >= self.player.max_health:
                                print("The adventurer feels extra rested.")
                                self.player.health += self.player.overheal_amount
                                print(self.player.health)
                                break
                            
                            print("The adventurer sleeps.")
                            self.player.health += self.player.rest_heal_amount
                            print("The adventurer gains ", self.player.rest_heal_amount," experience.")
                            break
                        
                        elif sit_command in ['repair','Repair','r','R', 'repair equipment', 'Repair Equipment']:
                            all_items = Items()
                            
                            broken = []
                            for broken_equipment in self.player.currently_equipped:
                                if broken_equipment[7] < getattr(all_items, broken_equipment[10])[7]:
                                    broken.append(broken_equipment)
                            
                            for broken_equipment in self.player.equipment:
                                if broken_equipment[7] < getattr(all_items, broken_equipment[10])[7]:
                                    broken.append(broken_equipment)
                                    
                            if not broken:
                                print("The adventurer has nothing to repair.")
                                continue
                            else:
                                cont_loop = True
                                while(cont_loop):
                                    print()
                                    for b_e in broken:
                                        print (b_e[0])
                                    print()
                                    
                                    repair_command = input("What would the adventurer like to repair? (Note: Items equipped are repaired first)")
                                    
                                    for item in broken:
                                        if repair_command == item[0]:
                                           
                                            item[7] += self.player.fix_amount
                                            
                                            print("The adventurer fixes a ", item[0]," by ", self.player.fix_amount, " for a total of", item[7], ".")
                                            
                                            cont_loop = False
                                            break
                                        else:
                                            print("The adventurer does not have a ", item[0],".")
                                            continue
                                break
                                    
                        elif sit_command in ['mediate','Mediate','m','M']:
                            print("The adventurer mediates.")
                            self.player.exp += self.player.rest_exp_amount
                            print("The adventurer gains ", self.player.rest_exp_amount," experience.")
                            break
                        else:
                            print("The adventurer cannot do that.")
                            continue
                    self.event_id = 'burned_bonfire'
                    print()   
                    break
                else:
                    self.event_id = 'event_bonfire'
                    self.player.burn_bonfire = False
                    print("The adventurer decides to return later.")
                    break
                
                
            elif self.event_id == 'event_random_positive':
                print("There is a + random event here.")
                print()
                break
            
            elif self.event_id == 'event_random_negative':
                print("There is a - random event here.")
                print()
                break
                
            elif self.event_id == 'event_empty':
                print("There is nothing here.")
                print()
                break
            
            elif self.event_id == 'dead_enemies':
                print('The adventurers past battle lies before them.')
                print()
                break
            
            elif self.event_id == 'empty_shop':
                print('An empty stall lies before the adventurer. It seems the shop has left.')
                print()
                break
            elif self.event_id == 'event_stairs':
                print()
                print('Before the Adventurer is a set of stairs descending into darkness.')
                command = input('Will the Adventurer take the descent? (Y/N)>')
                if command in ['y','Y','Yes','yes']:
                    print('The Adventurer descends.')
                    self.player.descend = True
                    print()
                    break
                else:
                    print()
                    print("The Adventurer decides to return later.")
                    break
            elif self.event_id == 'burned_bonfire':
                print('Ash lays where a fire once burned.')
                print()
                break
                
            else:
                print('unknown event')
                break
            