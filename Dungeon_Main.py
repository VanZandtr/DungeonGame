# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:36:40 2019

@author: rlv220
"""
from Dungeon_Generator import DungeonGenerator
from Dungeon_Events import Event
from Dungeon_Player import Player
from Dungeon_Skills import Skills
from Dungeon_Items import Items
import numpy as np
import math as math
import pickle as pickle
from os import path
player = Player()
skills = Skills()

def hint():
    res = "----------Hint----------"
    res += '\n'
    res +='Quit: q, Q, exit, Exit, quit, Quit'
    res += '\n'
    res +='Move North: north, North, move North, Move North, move north, Move north'
    res += '\n'
    res +='Move South: south, South, move South, Move South, move south, Move south'
    res += '\n'
    res +='Move East: east, East, move East, Move East, move east, Move east'
    res += '\n'
    res +='Move West: west, West, move West, Move West, move west, Move west'
    res += '\n'
    res +='Inventory: i, I, Inventory, inventory'
    res += '\n'
    res +='Skills: s, S, skills, Skills'
    res += '\n'
    res +='Equip: e, E, equip, Equip'
    res += '\n'
    res +='Unequip: u, U, unequip, Unequip'
    res += '\n'
    res +='Stuck?: stuck, Stuck, DELETE THIS AFTER MAP IS FIXED'
    res += '\n'
    res +='Save Game: SAV, sav, Sav'
    res += '\n'
    res +='Hint:display this message'
    res += '\n'
    res +="----------Hint----------"
    res += '\n'
    return res
    
def gen_new_map(matrix, x_coor, y_coor):
    matrix[:]='.'
    matrix[x_coor,y_coor] = '1'
    
def save_game(matrix, dungeon_map, current_room, previous_room, x_coor, y_coor):
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
    
def reset_map(matrix, bounds):
    for i in range(bounds):
        for j in range(bounds):
            if matrix[i,j] == '*':
                matrix[i,j] = '.'

def update_screen_map(matrix, bounds, x_coor, y_coor, map_markers):
    for i in range(bounds):
        for j in range(bounds):
            if matrix[i,j] not in map_markers:
                matrix[i,j]='.'
    matrix[x_coor,y_coor] = '1'
    
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
            res = '\n'
            res += 'The adventure has leveled up! Level:' + player_arg.level
            res += '\n'
            #give random loot?

        skills_to_remove = []

        for skill in range(len(player_arg.unknown_skills)):
            if player_arg.unknown_skills[skill][1] == player_arg.level:
                res += '\n'
                res += 'The adventurer has learned' + player_arg.unknown_skills[skill][0]
                res += '\n'
                
                #add the skill to known skills
                player_arg.known_skills.append(player_arg.unknown_skills[skill].copy())
                #remove the skill from unknown skills
                skills_to_remove.append(player_arg.unknown_skills[skill].copy())
        
        for remove in skills_to_remove:        
            player_arg.unknown_skills.remove(remove)
            

def get_gamesave(bool_load, dungeon_map, bounds, mapsize, need_class):
    if bool_load in True:
        matrix, dungeonmap, current_room, previous_room, x_coor, y_coor = load_game()
        return matrix, dungeonmap, current_room, previous_room, x_coor, y_coor
        
        #display hint
        hint()
        
        #print map to screen
        for i in range(bounds):
            for j in range(bounds):
                print(matrix[i,j],end='  ')
            print('\n')
    
    else:
        new_Dungeon = DungeonGenerator(mapsize)
        new_Dungeon.makeDungeon()
        dungeon_map = new_Dungeon.map
        
        return dungeon_map
        gen_new_map()
        hint()
        
        
def get_class(classes, need_class):
    while(need_class):
        res = 'What will the adventurer be this time?'
        for character_class in classes:
            res += str(character_class)
        
        command = input('>')
        
        if command in classes:
            res = 'The adventurer wishes to be a' + command + '? So be it...'
            
            Skills().getSkills(player,command)
            
            need_class = False
        else:
            res = 'The adventurer may not venture this path. Choose another.'
            need_class = True
        return command

def get_gamestate(dungeon_map, current_room, previous_room, x_coor, y_coor, mapsize, matrix, map_markers, bounds, room):            
    map_marker = '0'
    
    if player.level >= len(player.level_array):
        print('The adventurer has reached his true potential')
        
    else:
        #check if character should level up
       level_up(player)
       
       

    room = dungeon_map[current_room]
    ava_rooms = []
    
    new_Event = Event(room.room_type, player)
    new_Event.fetchEvent()
    
    if player.is_dead == True:
        print("The adventurer has died")
    
    if room.room_type == ('event_enemy_encounter' or 'event_enemy_encounter_boss') and player.ran_away == False:
        #if we get here we know the player has won the encounter
        room.room_type = 'dead_enemies'
        
    elif room.room_type == ('event_enemy_encounter' or 'event_enemy_encounter_boss') and player.ran_away == True:
        print('The adventurer flees to the previous room', previous_room)
        player.ran_away = False
        if room.north == previous_room:
            x_coor -= 1
        elif room.south == previous_room:
            x_coor += 1
        elif room.east == previous_room:
            y_coor += 1
        else:
            y_coor -= 1
            
        reset_map()
        update_screen_map()
        current_room = previous_room
    
    elif room.room_type == 'event_shop':
        #shop leaves
        room.room_type = 'empty_shop'
        
    elif (room.room_type == 'event_bonfire' and player.burn_bonfire == True):
        room.room_type = 'burned_bonfire'
        player.burn_bonfire = False
    
    elif room.room_type == 'event_bonfire' and player.burn_bonfire == False:
        print("HERE")
        map_marker = '^'
        
    elif room.room_type == 'event_stairs' and player.descend == False:
        map_marker = 'x'

    elif room.room_type == 'event_stairs' and player.descend == True:
        player.descend = False

        previous_room = 0
        current_room = 0
        
        
        new_Dungeon = DungeonGenerator(mapsize)
        new_Dungeon.makeDungeon()
        new_Dungeon.room_id = 0
        dungeon_map = new_Dungeon.map
        
        y_coor = math.floor(bounds/2)
        x_coor = math.floor(bounds/2)
      
        gen_new_map()
        
    
    if room.north != -1:
        ava_rooms.append("North")
        if matrix[x_coor - 1, y_coor] not in map_markers:
            matrix[x_coor - 1, y_coor] = '*'
            
    if room.south != -1:
        ava_rooms.append("South")
        if matrix[x_coor + 1, y_coor] not in map_markers:
            matrix[x_coor +1, y_coor] = '*'
            
    if room.east != -1:
        ava_rooms.append("East")
        if matrix[x_coor, y_coor + 1] not in map_markers:
            matrix[x_coor, y_coor + 1] = '*'
            
    if room.west != -1:
        ava_rooms.append("West")
        if matrix[x_coor, y_coor - 1] not in map_markers:
            matrix[x_coor, y_coor - 1] = '*'
            
    #print map to screen
    for i in range(bounds):
        for j in range(bounds):
            print(matrix[i,j],end='  ')
        print('\n')
    
    msg = 'There is a room to the: '
    for room in ava_rooms:
        msg += room
    
    return msg, dungeon_map, current_room, previous_room, x_coor, y_coor, matrix, room, map_marker

def main_loop(command):
    quit_flag = False
    ret = ""
    if command in ['q','Q','exit','Exit','Quit','quit']:
        ret = "quitting"
        quit_flag = True
        
    elif command in ['north', 'North', 'move North', 'Move North', 'move north', 'Move north']:
        ret = "The adventurer moves north."
       
        
    elif command in ['south', 'South', 'move South', 'Move South', 'move south', 'Move south']:
        ret = "The adventurer moves south."
        
    elif command in ['east', 'East', 'move East', 'Move East', 'move east', 'Move east']:
        ret = "The adventurer moves east."
        
    elif command in ['west', 'West', 'move West', 'Move West', 'move west', 'Move west']:
        ret = "The adventurer moves west."
        
    elif command in ['I', 'i', 'Inventory', 'inventory']:
        ret = "----------Inventory----------"
    
    elif command in ['U','u','unequip', 'Unequip']:
        ret = "Unequipping"
        
    elif command in ['E','e','equip', 'Equip']:
        ret = "Equiping"
                
    elif command in ['S', 's', 'Skills', 'skills']:
        ret = "----------Skills----------"
    
    elif command in ['H','h','hint', 'Hint']:
        ret = hint()
    
    elif command in ['Stuck', 'stuck']:
        ret = "HAVE THIS CHECK IF NO ROOM HAD THE STAIRS EVENT FIRST!"
        
    elif command in ['SAV', 'sav', 'Sav']:
        ret = "The adventurer has saved his progression"
        
    else:
        ret = "I am unsure what the adventurer wants."
    return quit_flag, ret