from Dungeon_Generator import DungeonGenerator
from Dungeon_Events import Event
from Dungeon_Player import Player
from Dungeon_Skills import Skills
from Dungeon_Items import Items
import numpy as np
import math as math
import pickle as pickle
from os import path
from Dungeon_Perm_Upgrades import Perm_Upgrade
import os


mapsize = 10
dungeon_map = {}
previous_room = 0
current_room = 0
need_class = True
max_level_alerted = False
classes = ['Wizard','Priest']
map_markers = ['0', 'x', '^']
player = Player()
skills = Skills()
perm_upgrades = Perm_Upgrade()
test = True
    
#test items
if test == True:
    items = Items()
    player.inventory.append(items.test_potion.copy())
    player.currently_equipped.append(items.rusty_sword.copy())
    player.currently_equipped.append(items.rusty_sword.copy())
    player.currently_equipped.append(items.rusty_helm.copy())
    player.equipment.append(items.rusty_chest.copy())

bounds = 11
matrix = np.chararray((bounds,bounds), unicode=True)
y_coor = math.floor(bounds/2)
x_coor = math.floor(bounds/2)
    
def gen_new_map():
    matrix[:]='.'
    matrix[x_coor,y_coor] = '1'
    
def save_game():
    arr = {key:value for key, value in player.__dict__.items() if not key.startswith('__') and not callable(key)}
    player_data = {}
    for key in arr:
        player_data[key] = getattr(player, key)
        
        
    #save
    with open("save_file.txt", "ab") as save_file:
        #clear file
        save_file.seek(0)
        save_file.truncate()
        #player data
        pickle.dump(player_data, save_file)
    save_file.close
        
    #gamestate
    matrix.dump("my_matrix.dat")
    
    with open("saved_dungeon_state.dat", "wb") as fp:
        #clear file
        fp.seek(0)
        fp.truncate()
        pickle.dump(dungeon_map, fp)
        pickle.dump(current_room, fp)
        pickle.dump(previous_room, fp)
        pickle.dump(x_coor, fp)
        pickle.dump(y_coor, fp)
    fp.close()

def load_perm_upgrades():
    perm_upgrades.load_upgrades(player)
    perm_upgrades.perm_key_applicator(['test'])

def load_game():
    load_file = open('save_file.txt', 'rb')      
    #load player data
    dir_content = pickle.load(load_file)
    for key in dir_content:
        setattr(player, key, dir_content[key])
    load_file.close()
    
    #load matrix data
    matrix = np.load("my_matrix.dat")
    
    #load map
    with open("saved_dungeon_state.dat", "rb") as fp:
        dungeon_map = pickle.load(fp)
        current_room = pickle.load(fp)
        previous_room = pickle.load(fp)
        x_coor = pickle.load(fp)
        y_coor = pickle.load(fp)
    fp.close()
    

    return matrix, dungeon_map, current_room, previous_room, x_coor, y_coor
    
def reset_map():
    for i in range(bounds):
        for j in range(bounds):
            if matrix[i,j] == '*':
                matrix[i,j] = '.'

def update_screen_map():
    for i in range(bounds):
        for j in range(bounds):
            if matrix[i,j] not in map_markers:
                matrix[i,j]='.'
    matrix[x_coor,y_coor] = '1'
        
def hint():
    print()
    print("----------Hint----------")
    print('Quit:','q, Q, exit, Exit, quit, Quit')
    print('Move North:','north, North, move North, Move North, move north, Move north')
    print('Move South:','south, South, move South, Move South, move south, Move south')
    print('Move East:','east, East, move East, Move East, move east, Move east')
    print('Move West:','west, West, move West, Move West, move west, Move west')
    print('Inventory:','i, I, Inventory, inventory')
    print('Skills:','s, S, skills, Skills')
    print('Equip:','e, E, equip, Equip')
    print('Upgrades:', 'u', 'U', 'upgrades', 'Upgrades')
    print('Unequip:','u, U, unequip, Unequip')
    print('Stuck?:','stuck', 'Stuck', "DELETE THIS AFTER MAP IS FIXED")
    print('Save Game:', 'SAV', 'sav', 'Sav')
    print('Hint:','display this message')
    print("----------Hint----------")
    print()
    
def level_up(player_arg):
    level = player_arg.level

    next_level = player_arg.level_array[level]
    
    #Increase Max Health and Mana
    player_arg.max_health += 30
    player_arg.max_mana += 10
    
    #Restore health and mana
    player_arg.current_mana = player_arg.max_mana
    player_arg.health = player_arg.max_health
    

    if player_arg.exp >= next_level:
        player_arg.level = level + 1
        
        if player_arg.level != 1:
            print()
            print('The adventure has leveled up:', 'Level:', player_arg.level)
            print()
            #give random loot?

        skills_to_remove = []

        for skill in range(len(player_arg.unknown_skills)):
            if player_arg.unknown_skills[skill][1] == player_arg.level:
                print()
                print('The adventurer has learned', player_arg.unknown_skills[skill][0])
                print()
                #add the skill to known skills
                player_arg.known_skills.append(player_arg.unknown_skills[skill].copy())
                #remove the skill from unknown skills
                skills_to_remove.append(player_arg.unknown_skills[skill].copy())
        
        for remove in skills_to_remove:        
            player_arg.unknown_skills.remove(remove)
            


''' GAME LOOP STARTS HERE'''
#check if file exists
load_new_dungeon = True
if path.exists("save_file.txt") == True:
    load_opt = input('Would the adventurer like to use a saved game?>')
    if load_opt in ['y','Y','yes','Yes','YES']:
        matrix, dungeon_map, current_room, previous_room, x_coor, y_coor = load_game()
        need_class = False
        hint()
        #print map to screen
        for i in range(bounds):
            for j in range(bounds):
                print(matrix[i,j],end='  ')
            print('\n')
        load_new_dungeon = False
    
if(load_new_dungeon == True):
    new_Dungeon = DungeonGenerator(mapsize)
    new_Dungeon.makeDungeon()
    dungeon_map = new_Dungeon.map
    gen_new_map()
    hint()

if path.exists("perm_upgrades.txt") == True:
    load_opt = input('Would the adventurer like to load their upgrades?>')
    if load_opt in ['y','Y','yes','Yes','YES']:
        load_perm_upgrades()
        
while(need_class):
        print('What will the adventurer be this time?>')
        for character_class in classes:
            print (character_class)
        command = input('>')
        string_command = str(command)
        print()
        if string_command in classes:
            print('The adventurer wishes to be a', string_command,'? So be it...')
            
            Skills().getSkills(player,string_command)
            
            need_class = False
        else:
            print('The adventurer may not venture this path. Choose another.')
            need_class = True
            
while(True):
    map_marker = '0'
    
    if player.level >= len(player.level_array):
        if (max_level_alerted == False):
            print('The adventurer has reached his true potential')
            max_level_alerted = True
    else:
        #check if character should level up
        level_up(player)

    map_room = dungeon_map[current_room]
    ava_rooms = []
    
    new_Event = Event(map_room.room_type, player)
    new_Event.fetchEvent()
    
    
    
    if player.is_dead == True:
        print("The adventurer has died")
        print()
        print("The adventurer may buy upgrades for gold")
        print()
        
        mt = perm_upgrades.mana_tree  
        ht = perm_upgrades.health_tree
        
        while(True):                
            print()
            print(mt)
            print()
            print(ht)
            print()
            
            upgrade_not_found = True
            not_enough_gold = False
            print("----------Upgrades----------")
            print()
            print('Gold:', player.gold)
            print()
            print('(q, Q, exit, Exit, Quit, quit) to leave.')
            command = input('What would the adventurer like to purchase?>')
            if command in ['q','Q','exit','Exit','Quit','quit']:
                #save upgrades
                perm_upgrades.save_upgrades(player)
                
                #delete files
                if path.exists("save_file.txt") == True:
                    os.remove("save_file.txt")
                    
                if path.exists("saved_dungeon_state.dat") == True:
                    os.remove("saved_dungeon_state.dat")
                    
                if path.exists("my_matrix.dat") == True:
                    os.remove("my_matrix.dat")
                
                print ("Goodbye")
                print()
                break
            
            else:
                for mu in mt:
                    if command == mu[1]:
                        if mu[3] > player.gold:
                            print('Not enough Gold')
                            not_enough_gold = True
                            break
                        else:
                            item_not_found = False
                            player.gold -= mu[3]
                            mt.remove(mu)
                            player.perm_upgrades.append(mu.copy())
                            print('A fine purchase.')
                            break
                    
                for  hu in ht:
                    if command == hu[1]:
                        if hu[3] > player.gold:
                            print('Not Enough Gold')
                            not_enough_gold = True
                            break
                        else:
                            item_not_found = False
                            player.gold -= hu[3]
                            ht.remove(hu)
                            player.perm_upgrades.append(hu.copy())
                            print('A fine purchase.')
                            break
                if item_not_found == True and not_enough_gold == False:
                    print('WHAT!')
                    continue

        break
    
    if map_room.room_type == ('event_enemy_encounter' or 'event_enemy_encounter_boss') and player.ran_away == False:
        #if we get here we know the player has won the encounter
        map_room.room_type = 'dead_enemies'
        
    elif map_room.room_type == ('event_enemy_encounter' or 'event_enemy_encounter_boss') and player.ran_away == True:
        print('The adventurer flees to the previous room', previous_room)
        player.ran_away = False
        if map_room.north == previous_room:
            x_coor -= 1
        elif map_room.south == previous_room:
            x_coor += 1
        elif map_room.east == previous_room:
            y_coor += 1
        else:
            y_coor -= 1
            
        reset_map()
        update_screen_map()
        current_room = previous_room
        continue
    
    elif map_room.room_type == 'event_shop':
        #shop leaves
        map_room.room_type = 'empty_shop'
        
    elif (map_room.room_type == 'event_bonfire' and player.burn_bonfire == True):
        map_room.room_type = 'burned_bonfire'
        player.burn_bonfire = False
    
    elif map_room.room_type == 'event_bonfire' and player.burn_bonfire == False:
        map_marker = '^'
        
    elif map_room.room_type == 'event_stairs' and player.descend == False:
        map_marker = 'x'

    elif map_room.room_type == 'event_stairs' and player.descend == True:
        player.descend = False

        previous_room = 0
        current_room = 0

        new_Dungeon.room_id = 0
        new_Dungeon = DungeonGenerator(mapsize)
        new_Dungeon.makeDungeon()
        dungeon_map = new_Dungeon.map
        
        y_coor = math.floor(bounds/2)
        x_coor = math.floor(bounds/2)
      
        gen_new_map()
    
        continue
        
    
    if map_room.north != -1:
        ava_rooms.append("North")
        if matrix[x_coor - 1, y_coor] not in map_markers:
            matrix[x_coor - 1, y_coor] = '*'
            
    if map_room.south != -1:
        ava_rooms.append("South")
        if matrix[x_coor + 1, y_coor] not in map_markers:
            matrix[x_coor +1, y_coor] = '*'
            
    if map_room.east != -1:
        ava_rooms.append("East")
        if matrix[x_coor, y_coor + 1] not in map_markers:
            matrix[x_coor, y_coor + 1] = '*'
            
    if map_room.west != -1:
        ava_rooms.append("West")
        if matrix[x_coor, y_coor - 1] not in map_markers:
            matrix[x_coor, y_coor - 1] = '*'
            
    #print map to screen
    for i in range(bounds):
        for j in range(bounds):
            print(matrix[i,j],end='  ')
        print('\n')
    
    print('There is a room to the:', end = " ")
    for room in ava_rooms:
        print(room, end=" ")
    
    command = input('What would the adventurer like to do?>')
    
    if command in ['q','Q','exit','Exit','Quit','quit']:
        print()
        quit_command = input('The adventurer will lose everything that is not saved. Is the adventurer sure?>' )
        if quit_command in ['y','Y','yes','Yes']:
            print("Goodbye friend, may he follow...")
            break
        else:
            continue
    
    elif command in ['north', 'North', 'move North', 'Move North', 'move north', 'Move north']:
        print()
        if map_room.north != -1:
            print("The adventurer moves north.")
            matrix[x_coor, y_coor] = map_marker
            x_coor-=1
            matrix[x_coor, y_coor] = '1'
            reset_map()
            previous_room = current_room
            current_room = map_room.north
            print()
        else:
            print("The adventurer may not move this way.")
            print()
            continue
        
    elif command in ['south', 'South', 'move South', 'Move South', 'move south', 'Move south']:
        print()
        if map_room.south != -1:
            print("The adventurer moves south.")
            matrix[x_coor, y_coor] = map_marker
            x_coor+=1
            matrix[x_coor, y_coor] = '1'
            reset_map()
            previous_room = current_room
            current_room = map_room.south
            print()
        else:
            print("The adventurer may not move this way.")
            print()
            continue
        
    elif command in ['east', 'East', 'move East', 'Move East', 'move east', 'Move east']:
        print()
        if map_room.east != -1:
            print("The adventurer moves east.")
            matrix[x_coor, y_coor] = map_marker
            y_coor+=1
            matrix[x_coor, y_coor] = '1'
            reset_map()
            previous_room = current_room
            current_room = map_room.east
            print()
        else:
            print("The adventurer may not move this way.")
            print()
            continue
        
    elif command in ['west', 'West', 'move West', 'Move West', 'move west', 'Move west']:
        print()
        if map_room.west != -1:
            print("The adventurer moves west.")
            matrix[x_coor, y_coor] = map_marker
            y_coor-=1
            matrix[x_coor, y_coor] = '1'
            reset_map()
            previous_room = current_room
            current_room = map_room.west
            print()
        else:
            print("The adventurer may not move this way.")
            print()
            continue
    elif command in ['U', 'u', 'Upgrades', 'upgrades']:
        if len(player.perm_upgrades) == 0:
            print("The Adventurer has not upgrades")
        else:
            print("------Upgrades--------")
            print(player.perm_upgrades)
        #TEST#
        print("Granting 10000 gold and killing player")
        player.gold = 10000
        player.is_dead = True
        continue
        
    elif command in ['I', 'i', 'Inventory', 'inventory']:
        print()
        print("----------Inventory----------")
        print('Class:', player.player_class)
        print('Level:', player.level)
        print('Health:', player.health)
        print('Gold:', player.gold)
        
        print()
        print('Currently Equipped: ')
        if len(player.currently_equipped) == 0:
            print("The adventurer has nothing equipped")
        else:
            for currently_equipped in player.currently_equipped:
                items.Equipment_Printout(currently_equipped)
        print()
        
        print()
        print('Equipment: ')
        if len(player.equipment) == 0:
            print("The adventurer has no equipment")
        
        else:
            items = Items()
            for item in player.equipment:
                items.Equipment_Printout(item)
        print()
        
        print('Inventory: ')
        if len(player.inventory) == 0:
            print("The adventurer has nothing")
            
        else:
            for item in player.inventory:
                if item[1] == "item":
                    items.Item_Printout(item)
                else:
                    items.Equipment_Printout(item)
                
        print("----------Inventory----------")
        print()
    
    elif command in ['U','u','unequip', 'Unequip']:
        print()
        if len(player.currently_equipped) == 0:
            print("The adventurer has nothing equipped")
            
        else:
            for ae in player.currently_equipped:
                print(ae)
                
            unequip = input('What would the adventurer like to unequip?>')
            
            item_found = False
            for e in player.currently_equipped:
                print(e[0])
                if unequip == e[0]:
                    player.currently_equipped.remove(e)
                    player.equipment.append(e.copy())
                    print()
                    print("The adventurer unequips their ", unequip)
                    item_found = True
                    break
            if item_found == False:
                    print("The adventurer doesn't have that")

        print()            
        
    elif command in ['E','e','equip', 'Equip']:
        if len(player.equipment) == 0:
            print()
            print("The adventurer has nothing equip")
            print()
            continue

        print()
        print('Equipment: ')
        for item in player.equipment:
           items.Equipment_Printout(item)
        print()
        
        item_not_found = True
        break_loop_flag = False
        
        equip = input('What would the adventurer like to equip?>')
        for e in player.equipment:
            if equip == e[0]:
                item_not_found = False
                print('item found')
                print()
                                
                if len(player.currently_equipped) == 0:
                    player.equipment.remove(e);
                    player.currently_equipped.append(e.copy())
                else:
                    for currently_equipped in player.currently_equipped:
                        if break_loop_flag == True:
                            break
                        
                        if currently_equipped[1] == e[1]:
                            print()
                            #check if hand
                            if e[1] == 'hand':
                                hand_counter = 0;
                                for current_hands_equipped in player.currently_equipped:
                                    if current_hands_equipped[1] == 'hand':
                                        hand_counter+=1
                                if hand_counter == 2:
                                    unequip_hand_check = input('What would the adventurer like to unequipped a weapon? (Y/N)>')
                                    if unequip_hand_check in ['y', 'Y', 'Yes', 'yes']:
                                        for get_hands in player.currently_equipped:
                                            if get_hands[1] == 'hand':
                                                items.Equipment_Printout(get_hands)
                                        unequip_hand = input('Which weapon would the adventurer like to unequip?>')
                                        for current_hands_equipped in player.currently_equipped:
                                            if unequip_hand == current_hands_equipped[0]:
                                                player.equipment.append(current_hands_equipped.copy());
                                                player.currently_equipped.remove(current_hands_equipped);
                                                player.equipment.remove(e)
                                                player.currently_equipped.append(e.copy())
                                                break_loop_flag = True
                                                break
                                    else:
                                        break
                                else:
                                    player.equipment.remove(e)
                                    player.currently_equipped.append(e.copy())
                                    break
                            else:
                                unequip_hand_check = input('What would the adventurer like to unequipped a ' + e[1] + ' ? (Y/N)>')
                                if unequip_hand_check in ['y', 'Y', 'Yes', 'yes']:
                                    for get_equipment in player.currently_equipped:
                                        if get_equipment[1] == e[1]:
                                            items.Equipment_Printout(get_equipment)
                                        unequip = input('Which ' + e[1] + ' would the adventurer like to unequip?>')
                                        for ce in player.currently_equipped:
                                            if unequip == ce[0]:
                                                player.equipment.append(ce.copy());
                                                player.currently_equipped.remove(ce);
                                                player.equipment.remove(e)
                                                player.currently_equipped.append(e.copy())
                                                break_loop_flag = True
                                                break
                                                    
                        else:
                            player.equipment.remove(e)
                            player.currently_equipped.append(e.copy())
                            break
                break
        if item_not_found == True:                
            print('The adventurer does not have that')
        print()
        
        
                
    elif command in ['S', 's', 'Skills', 'skills']:
        print()
        print("----------Skills----------")
        print('Exp:', player.exp)
        print('Level:', player.level)
        print('Next Level up:', player.level_array[player.level])
        print('Max Mana:', player.max_mana)
        print('Mana:', player.current_mana)
        print()
        
        print('Skills: ')
        if len(player.known_skills) == 0:
            print("The adventurer has no skills")
            
        else:
            for skill in range(len(player.known_skills)):    
                skills.Skill_Printout(player.known_skills[skill])
        
        print()
        print('Unknown Skills: ')
        for skill in range(len(player.unknown_skills)):
            skills.Skill_Printout(player.unknown_skills[skill])
            
        print("----------Skills----------")
        print()
    elif command in ['H','h','hint', 'Hint']:
        hint()
    
    elif command in ['Stuck', 'stuck']:
        print("HAVE THIS CHECK IF NO ROOM HAD THE STAIRS EVENT FIRST!")
        map_room.room_type = 'event_stairs'
        player.descend = True
        
    elif command in ['SAV', 'sav', 'Sav']:
        print("The adventurer has saved his progression")
        save_game()
        
    else:
        print()
        print("I am unsure what the adventurer wants.")
        continue
