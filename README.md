# Another Rogue-Lite Dungeon Crawler
A game created and tested by Raymond Van Zandt.

## Introduction
You awake to unknown dungeon guided by an unknown voice. Face monsters and hazards as you level up gaining new weapons and learning new skills. Random encounters and bosses are met along the way as you search room to room floor by floor. Can you find the way out?

## Features
- Class System w/ Multiple Classes (Wizard & Priest)
- Health & Spell System (Specific to Class)
- Item, Equipment, Misc. Inventories
- Combat System
- Permadeath
- Movement System (Nostalgic of Zork)
- Shops
- Room Remembering (i.e. enemies stay dead, shop can't be visited twice)
- Randomized Dungeon
- Multiple Enemy types

## How to Play
1.) Download files  
2.) run python on Dungeon_Crawler_Main.py  
3.) Follow hints to get started  
4.) Enjoy!  

## File Description
- Basic_Room.py
   * Room Object
- Dungeon_Crawler_Main.py 
   * Main script 
   * Handles Main "UI" Loop
- Dungeon_Events.py 
   * Checks each room for its random event and handles it
- Dungeon_Generator.py
   * Dungeon Creation script 
   * Randomizes layout and events
- Dungeon_Items.py 
   * Holds all Items and Equipments to be called
- Dungeon_Minions.py 
   * Handles all minions and bosses
   * Combat loop
- Dungeon_Player.py 
   * Player Object
- Dungeon_Skills.py 
   * Holds all skills and class options.

## Future Work
- Multiple floors w/ exit           (Added May 2019)
- Implement more room types (traps, random encounters, etc.)(Added May 2019)  
- Unique Boss fights                (Added May 2019)  
- Furthur class skill design        (Added May 2019)  
- Lore and Item/Equipment creation  (Added May 2019)  
- Turn Dungeon_Minions.py into two scripts (Combat and Minions). (Added May 2019)  
- Change Dungeon_Minions.py, Dungeon_Skills.py, and Dungeon_Items.py into Tables.(Added May 2019) 
- Make items/equipment usable in combat           (Added May 2019)
