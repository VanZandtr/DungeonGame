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
        while(True):
            print("event:", self.event_id)
            
            if self.event_id is 'event_enemy_encounter':
                random_minion = random.uniform(0,1)
                
                if random_minion < 0.5:
                    new_minion = Minions('rat', self.player)
                    return new_minion.spawnMinion()
                    
                else:
                    new_minion = Minions('thief', self.player)
                    new_minion.spawnMinion()
                    
                break
                
            elif self.event_id is 'event_enemy_encounter_boss':
                random_boss = random.uniform(0,1)
                
                if random_boss < 0.5:
                    new_minion = Minions('big_rat')
                    return new_minion.spawnBoss(self.player)
                    
                else:
                    new_minion = Minions('theif_boss')
                    return new_minion.spawnBoss(self.player)
                    
                break
                
            elif self.event_id is 'event_shop':
                item_Class = Items()
                print("There is a shop here.")
                print()
                
                scripted_phrases = ['LOOK! NO TOUCH! Unless you have coin....', 'WHO BE SNOOPI-. Oh Hello!', '*Rumaging* Take a look, but NO TOUCH! no touch.']
                phrase = random.choice(scripted_phrases)
                print (phrase)
                print()
                print("----------Shop----------")
                
                #Test shop
                self.player.gold = 10000
                
                equipment_arr = random.sample(item_Class.veryeasy_shop_equipment, 5)
                item_arr = random.sample(item_Class.veryeasy_shop_item, 5)
                while(True):                
                    print()
                    print('Equipment [name, type, cost, damage added, addition max health, additional max mana, mana restore, armor rating (10), durability, additional properties, description]:')
                    for e in equipment_arr:
                        print(e)
                    print()
                    print('Items [name, type, cost, max health increase, max mana increase, temp health increase, temp mana increase, description]:')
                    for i in item_arr:
                        print(i)
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
                
            elif self.event_id is 'event_bonfire':
                sit_command = input("A bonfire smolders gentle before the Adventurer. Will the Adventurer rest? (Y/N)>")
                if sit_command in ['y','Y','Yes','yes']:
                    print('The Adventurer sits.')
                    self.player.burn_bonfire = True
                    print("The adventure repairs(Weapon/Armor Durability), sleeps(HP), meditates (EXP)")
                    break
                else:
                    print("The Adventurer decides to return later.")
                    break
                
                
            elif self.event_id is 'event_random_positive':
                print("There is a random event here.")
                break
                
            elif self.event_id is 'event_empty':
                print("There is nothing here.")
                break
            
            elif self.event_id is 'dead_enemies':
                print('The adventurers past battle lies before them.')
                break
            
            elif self.event_id is 'empty_shop':
                print('An empty stall lies before the adventurer. It seems the shop has left.')
                break
            elif self.event_id is 'event_stairs':
                print('Before the Adventurer is a set of stairs descending into darkness.')
                command = input('Will the Adventurer take the descent? (Y/N)>')
                if command in ['y','Y','Yes','yes']:
                    print('The Adventurer descends.')
                    self.player.descend = True
                    break
                else:
                    print("The Adventurer decides to return later.")
                    break
            elif self.event_id is 'burned_bonfire':
                print('Ash lays where a fire once burned.')
                break

                    
                break
                
            else:
                print('unknown event')
                break
            