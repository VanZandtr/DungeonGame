from Dungeon_Generator import DungeonGenerator
from Dungeon_Events import Event
from Dungeon_Player import Player
from Dungeon_Skills import Skills
from Dungeon_Items import Items


mapsize = 10
new_Dungeon = DungeonGenerator(mapsize)
new_Dungeon.makeDungeon()
dungeon_map = new_Dungeon.map

'''
print("----------final----------")
for room in dungeon_map:
    print("id",room.room_id)
    print("north",room.north)
    print("south",room.south)
    print("east",room.east)
    print("west",room.west)
    print()
    print()
print("----------final----------")
'''

previous_room = 0
current_room = 0

need_class = True
max_level_alerted = False
classes = ['Wizard','Priest']

player = Player()
skills = Skills()

test = True

#test items
if test is True:
    items = Items()
    player.inventory.append(items.test_potion)
    player.currently_equipped.append(items.rusty_sword.copy())
    player.currently_equipped.append(items.rusty_sword.copy())


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
    print('Unequip:','u, U, unequip, Unequip')
    print('Hint:','display this message')
    print("----------Hint----------")
    print()
    
def level_up(player_arg):
    level = player_arg.level

    next_level = player_arg.level_array[level]

    if player_arg.exp >= next_level:
        player_arg.level = level + 1
        
        if player_arg.level is not 1:
            print()
            print('The adventure has leveled up:', 'Level:', player_arg.level)
            print()
            #give random loot?

        skills_to_remove = []

        for skill in range(len(player_arg.unknown_skills)):
            if player_arg.unknown_skills[skill][1] is player_arg.level:
                print()
                print('The adventurer has learned', player_arg.unknown_skills[skill][0])
                print()
                #add the skill to known skills
                player_arg.known_skills.append(player_arg.unknown_skills[skill])
                #remove the skill from unknown skills
                skills_to_remove.append(player_arg.unknown_skills[skill])
        
        for remove in skills_to_remove:        
            player_arg.unknown_skills.remove(remove)
            
        
hint()

while(need_class):
        print('What will the adventurer be this time?>')
        for character_class in classes:
            print (character_class)
        command = input('>')
        string_command = str(command)
        print()
        if string_command in classes:
            print('The adventurer wishes to be a', string_command,'so be it...')
            
            Skills().getSkills(player,string_command)
            
            need_class = False
        else:
            print('The adventurer may not venture this path. Choose another.')
            need_class = True
        
        
while(True):
    
    if player.level >= len(player.level_array):
        if (max_level_alerted is False):
            print('The adventurer has reached his true potential')
            max_level_alerted = True
    else:
        #check if character should level up
        level_up(player)
    
    
    map_room = dungeon_map[current_room]
    ava_rooms = []
    
    print('The adventurer is in room',current_room,'.')
    
    new_Event = Event(map_room.room_type, player)
    new_Event.fetchEvent()
    
    if player.is_dead is True:
        print("The adventurer has died")
        break
    
    if map_room.room_type is ('event_enemy_encounter' or 'event_enemy_encounter_boss') and player.ran_away is False:
        #if we get here we know the player has won the encounter
        map_room.room_type = 'dead_enemies'
        
    elif map_room.room_type is ('event_enemy_encounter' or 'event_enemy_encounter_boss') and player.ran_away is True:
        print('The adventurer flees to the previous room', previous_room)
        player.ran_away = False
        current_room = previous_room
        continue
    
    elif map_room.room_type is 'event_shop':
        #shop leaves
        map_room.room_type = 'empty_shop'
        
    
    if map_room.north is not -1:
        ava_rooms.append("North")
    if map_room.south is not -1:
        ava_rooms.append("South")
    if map_room.east is not -1:
        ava_rooms.append("East")
    if map_room.west is not -1:
        ava_rooms.append("West")
    
    print('There is a room to the:', end = " ")
    for room in ava_rooms:
        print(room, end=" ")
    
    command = input('What would the adventurer like to do?>')
    
    if command in ['q','Q','exit','Exit','Quit','quit']:
        print()
        quit_command = input('The adventurer will lose everything. Is the adventurer sure?>' )
        if quit_command in ['y','Y','yes','Yes']:
            print("Goodbye friend, may he follow...")
            break
        else:
            continue
    
    elif command in ['north', 'North', 'move North', 'Move North', 'move north', 'Move north']:
        print()
        if map_room.north is not -1:
            print("The adventurer moves north.")
            previous_room = current_room
            current_room = map_room.north
            print()
        else:
            print("The adventurer may not move this way.")
            print()
            continue
        
    elif command in ['south', 'South', 'move South', 'Move South', 'move south', 'Move south']:
        print()
        if map_room.south is not -1:
            print("The adventurer moves south.")
            previous_room = current_room
            current_room = map_room.south
            print()
        else:
            print("The adventurer may not move this way.")
            print()
            continue
        
    elif command in ['east', 'East', 'move East', 'Move East', 'move east', 'Move east']:
        print()
        if map_room.east is not -1:
            print("The adventurer moves east.")
            previous_room = current_room
            current_room = map_room.east
            print()
        else:
            print("The adventurer may not move this way.")
            print()
            continue
        
    elif command in ['west', 'West', 'move West', 'Move West', 'move west', 'Move west']:
        print()
        if map_room.west is not -1:
            print("The adventurer moves west.")
            previous_room = current_room
            current_room = map_room.west
            print()
        else:
            print("The adventurer may not move this way.")
            print()
            continue
        
    elif command in ['I', 'i', 'Inventory', 'inventory']:
        print()
        print("----------Inventory----------")
        print('Class:', player.player_class)
        print('Level:', player.level)
        print('Health:', player.health)
        print('Exp:', player.exp)
        print('Next Level up:', player.level_array[player.level])
        print('Gold:', player.gold)
        
        print()
        print('Currently Equipped: ')
        if len(player.currently_equipped) is 0:
            print("The adventurer has nothing equipped")
        else:
            for currently_equipped in player.currently_equipped:
                print(currently_equipped)
        print()
        
        print()
        print('Equipment: ')
        if len(player.equipment) is 0:
            print("The adventurer has no equipment")
        
        else:
            for item in player.equipment:
                print(item)
        print()
        
        print('Inventory: ')
        if len(player.inventory) is 0:
            print("The adventurer has nothing")
            
        else:
            for item in player.inventory:
                print(item)
                
        print("----------Inventory----------")
        print()
    
    elif command in ['U','u','unequip', 'Unequip']:
        print()
        if player.weapon_equipped is 'none':
            print("The adventurer has nothing equipped")
        else:
            print("The adventurer unequips their weapon")
            player.equipment.append(player.weapon_equipped)
            player.weapon_equipped = 'none'
        print()            
        
    elif command in ['E','e','equip', 'Equip']:
        if len(player.equipment) is 0:
            print()
            print("The adventurer has nothing equip")
            print()
            continue

        print()
        print('Equipment: ')
        for item in player.equipment:
            print(item)
        print()
        
        item_not_found = True
        break_loop_flag = False
        
        equip = input('What would the adventurer like to equip?>')
        for e in player.equipment:
            if equip == e[0]:
                item_not_found = False
                print('item found')
                print()
                                
                if len(player.currently_equipped) is 0:
                    player.equipment.remove(e);
                    player.currently_equipped.append(e)
                else:
                    print("in else statment")
                    for currently_equipped in player.currently_equipped:
                        if break_loop_flag is True:
                            break
                        
                        if currently_equipped[1] == e[1]:
                            print('same item found')
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
                                                print(get_hands)
                                        unequip_hand = input('Which weapon would the adventurer like to unequip?>')
                                        for current_hands_equipped in player.currently_equipped:
                                            if unequip_hand == current_hands_equipped[0]:
                                                player.equipment.append(current_hands_equipped);
                                                player.currently_equipped.remove(current_hands_equipped);
                                                player.equipment.remove(e)
                                                player.currently_equipped.append(e)
                                                break_loop_flag = True
                                                break
                                    else:
                                        break
                                else:
                                    player.equipment.remove(e)
                                    player.currently_equipped.append(e)
                                    break
                            else:
                                unequip_hand_check = input('What would the adventurer like to unequipped a ' + e[1] + ' ? (Y/N)>')
                                if unequip_hand_check in ['y', 'Y', 'Yes', 'yes']:
                                    for get_equipment in player.currently_equipped:
                                        if get_equipment[1] == e[1]:
                                            print(get_equipment)
                                        unequip = input('Which ' + e[1] + ' would the adventurer like to unequip?>')
                                        for ce in player.currently_equipped:
                                            if unequip == ce[0]:
                                                player.equipment.append(ce);
                                                player.currently_equipped.remove(ce);
                                                player.equipment.remove(e)
                                                player.currently_equipped.append(e)
                                                break_loop_flag = True
                                                break
                                                    
                        else:
                            player.equipment.remove(e)
                            player.currently_equipped.append(e)
                            break
                break
        if item_not_found == True:                
            print('The adventurer does not have that')
        print()
        
        
                
    elif command in ['S', 's', 'Skills', 'skills']:
        print()
        print("----------Skills----------")
        print('Max Mana:', player.max_mana)
        print('Mana:', player.current_mana)
        print()
        
        print('Skills: ')
        if len(player.known_skills) is 0:
            print("The adventurer has no skills")
            
        else:
            for skill in range(len(player.known_skills)):
                min_damage = str(player.known_skills[skill][3])
                max_damage = str(player.known_skills[skill][4])
                description = player.known_skills[skill][9]
                name = player.known_skills[skill][0]
                level = player.known_skills[skill][1]
                cost = player.known_skills[skill][2]
                
                if min_damage == max_damage:
                    print('Skill:', name,'Level:', level,'Mana Cost:', cost, 'Damage:', min_damage, '~ ' + description)
                
                else:
                    print('Skill:', name,'Level:', level,'Mana Cost:', cost, 'Damage:', min_damage + '-' + max_damage, '~ ' + description)
        
        print()
        print('Unknown Skills: ')
        for skill in range(len(player.unknown_skills)):
            min_damage = str(player.unknown_skills[skill][3])
            max_damage = str(player.unknown_skills[skill][4])
            description = player.unknown_skills[skill][9]
            name = player.unknown_skills[skill][0]
            level = player.unknown_skills[skill][1]
            cost = player.unknown_skills[skill][2]
            
            if min_damage == max_damage:
                print('Skill:', name,'Level:', level,'Mana Cost:', cost, 'Damage:', min_damage, '~ ' + description)
                
            else:
                print('Skill:', name,'Level:', level,'Mana Cost:', cost, 'Damage:', min_damage + '-' + max_damage, '~ ' + description)
            
        print("----------Skills----------")
        print()
    elif command in ['H','h','hint', 'Hint']:
        hint()
        
    else:
        print()
        print("I am unsure what the adventurer wants.")
        continue
