# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:36:25 2019

@author: Raymond
"""
import random
from Basic_Room import Room

#Make adding doors a 50/50

class DungeonGenerator:
    def __init__(self, size):
        self.room_id = 0
        self.size = size
        self.map = []
        #self.event = ['event_enemy_encounter', 'event_enemy_encounter', 'event_enemy_encounter', 'event_enemy_encounter_boss', 'event_shop', 'event_bonfire', 'event_bonfire', 'event_random_positive', 'event_random_positive', 'event_empty', 'event_empty']
        self.event = ['event_enemy_encounter']
        self.has_stair_event = False
        
    def makeDungeon(self):
        #reset events on stair descent
        events = self.event.copy()
        
        self.has_stair_event = False
        counter = 0
        loop = iter(range(0,self.size))
        for x in loop:
            counter+=1;
            
            north_flag = random.random()
            south_flag = random.random()
            east_flag = random.random()
            west_flag = random.random()
            north_id = -1
            south_id = -1
            east_id = -1
            west_id = -1
            current_room_id = self.room_id           
            
            if (north_flag and south_flag and east_flag and west_flag) < .5:
                random_room = random.uniform(0,4)
                if random_room < 1:
                    north_flag = 1
                elif random_room < 2:
                    south_flag = 1
                elif random_room < 3:
                    east_flag = 1
                elif random_room < 4:
                    west_flag = 1
                                    
            if len(self.map) is 0:
            
                rooms_to_add = [i for i in[north_flag, south_flag, east_flag, west_flag] if i >=.5]
                
                
                if north_flag in rooms_to_add:
                    new_event = random.choice(events)
                    if new_event == "event_stairs":
                        events.remove("event_stairs")
                        self.has_stair_event = True
                        
                    north_id = self.room_id + 1
                    north_room = Room(north_id, -1, current_room_id, -1, -1, new_event)
                    self.room_id += 1
                    counter+=1
                    next(loop, None)
                    self.map.insert(self.room_id, north_room)
                    
                if south_flag in rooms_to_add:
                    new_event = random.choice(events)
                    if new_event == "event_stairs":
                        events.remove("event_stairs")
                        self.has_stair_event = True
                    
                    south_id = self.room_id + 1
                    south_room = Room(south_id, current_room_id, -1, -1, -1, new_event)
                    self.room_id += 1
                    counter+=1
                    next(loop, None)
                    self.map.insert(self.room_id, south_room)
                    
                if east_flag in rooms_to_add:
                    new_event = random.choice(events)
                    if new_event == "event_stairs":
                        events.remove("event_stairs")
                        self.has_stair_event = True
                        
                    east_id = self.room_id + 1
                    east_room = Room(east_id, -1, -1, -1, current_room_id, new_event)
                    self.room_id += 1
                    counter+=1
                    next(loop, None)
                    self.map.insert(self.room_id, east_room)
                    
                if west_flag in rooms_to_add:
                    new_event = random.choice(events)
                    if new_event == "event_stairs":
                        events.remove("event_stairs")
                        self.has_stair_event = True
                    
                    west_id = self.room_id + 1
                    west_room = Room(west_id, -1, -1, current_room_id, -1,new_event)
                    self.room_id += 1
                    counter+=1
                    next(loop, None)
                    self.map.insert(self.room_id, west_room)
            
                first_room = Room(current_room_id, north_id, south_id, east_id, west_id, 'event_empty')
                self.map.insert(0, first_room)
                
            else:
                while(True):
                    random_room = random.choice(self.map)
                    random_door = random.uniform(0,4)
                    
                    new_event = random.choice(events)
                    
                    if counter == 9 and self.has_stair_event == False:
                        new_event = 'event_stairs'
                        self.has_stair_event = True
                   
                    elif new_event == 'event_stairs' and self.has_stair_event == False:
                        events.remove('event_stairs')
                        self.has_stair_event = True
                        new_event = 'event_stairs'
                        
                    else:
                        pass

                    
                    if random_door < 1 and random_room.north is -1:
                        north_id = self.room_id + 1
                        north_room = Room(north_id, -1, random_room.room_id, -1, -1, new_event)
                        random_room.north = north_id
                        self.room_id += 1
                        self.map.insert(self.room_id, north_room)
                        
                        
                        if random_room.east is not -1 and self.map[random_room.east].north is not -1:
                            self.map[self.map[random_room.east].north].west = north_id
                            north_room.east = self.map[random_room.east].north
                            
                        if random_room.west is not -1 and self.map[random_room.west].north is not -1:
                            self.map[self.map[random_room.west].north].east = north_id
                            north_room.west = self.map[random_room.west].north
                            
                        break 
                    
                    elif random_door < 2 and random_room.south is -1:
                        south_id = self.room_id + 1
                        south_room = Room(south_id, random_room.room_id, -1, -1, -1, new_event)
                        random_room.south = south_id
                        self.room_id += 1
                        self.map.insert(self.room_id, south_room)
                        
                        
                        if random_room.east is not -1 and self.map[random_room.east].south is not -1:
                            self.map[self.map[random_room.east].south].west = south_id
                            south_room.east = self.map[random_room.east].south
                            
                        if random_room.west is not -1 and self.map[random_room.west].south is not -1:
                            self.map[self.map[random_room.west].south].east = south_id
                            south_room.west = self.map[random_room.west].south
                        
                        break
                    
                    elif random_door < 3 and random_room.east is -1:
                        east_id = self.room_id + 1
                        east_room = Room(east_id, -1, -1, -1, random_room.room_id, new_event)
                        random_room.east = east_id
                        self.room_id += 1
                        self.map.insert(self.room_id, east_room)
                        
                        
                        if random_room.north is not -1 and self.map[random_room.north].east is not -1:
                            self.map[self.map[random_room.north].east].south = east_id
                            east_room.north = self.map[random_room.north].east
                            
                        if random_room.south is not -1 and self.map[random_room.south].east is not -1:
                            self.map[self.map[random_room.south].east].north = east_id
                            east_room.south = self.map[random_room.south].east
                        break
                    
                    elif random_door < 4 and random_room.west is -1:
                        west_id = self.room_id + 1
                        west_room = Room(west_id, -1, -1, random_room.room_id, -1, new_event)
                        random_room.west = west_id
                        self.room_id += 1
                        self.map.insert(self.room_id, west_room)

                        if random_room.north is not -1 and self.map[random_room.north].west is not -1:
                            self.map[self.map[random_room.north].west].south = west_id
                            west_room.north = self.map[random_room.north].west
                            
                        if random_room.south is not -1 and self.map[random_room.south].west is not -1:
                            self.map[self.map[random_room.south].west].north = west_id
                            west_room.south = self.map[random_room.south].west
                        break
            
           
            '''
        print("----------final----------")
        for room in self.map:
            print("id",room.room_id)
            print("north",room.north)
            print("south",room.south)
            print("east",room.east)
            print("west",room.west)
            print()
            print()
        print("----------final----------")
        '''
            
    
                    
                
                
                
                        
                
                
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    
                