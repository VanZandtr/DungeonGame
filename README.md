# Another <s>Rogue-Lite</s> Dungeon Crawler
A game created and tested by Raymond Van Zandt.

## Introduction
You awake to unknown dungeon guided by an unknown voice. Face monsters and hazards as you level up gaining new weapons and learning new skills. Random encounters and bosses are met along the way as you search room to room floor by floor. Can you find the way out?

## Features
- Class System w/ Multiple Classes (Wizard & Priest)
- Health & Spell System (Specific to Class)
- Item, Equipment, Misc. Inventories
- Combat System
- Permadeath (Needs to be updated with new save system)
- Movement System (Nostalgic of Zork)
- Shops
- Room Remembering (i.e. enemies stay dead, shop can't be visited twice)
- Randomized Dungeon
- Multiple Enemy types
- Multiple Floors
- Real Time Map
- Game Saving
- Permanent Progression

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
- my_matrix.dat
   * Holds save info for map
- saved_dungeon_state.dat
   * Holds save info for dungeon layout and gamestate
- save_file.txt
   * Holds save info for player stats/equipment/skills
- perm_upgrades.txt
   * Holds Permanent Upgrades between playthroughs

## Future Work
- <s>Multiple floors           (Added May 2019)</s> (Completed 7/3/2019)
- Implement more room types (traps, random encounters, etc.)(Added May 2019)  
- Unique Boss fights                (Added May 2019)  
- Furthur class skill design        (Added May 2019)  
- Lore and Item/Equipment creation  (Added May 2019)  
- Turn Dungeon_Minions.py into two scripts (Combat and Minions). (Added May 2019)  
- Change Dungeon_Minions.py, Dungeon_Skills.py, and Dungeon_Items.py into Tables (ie Database).(Added May 2019) 
- <s>Make items/equipment usable in combat           (Added June 2019)</s> (Completed 7/2/2019)
- Add Exit (Added 7/3/2019)
- Update Permadeath (i.e. just delete the files) (Added 11/12/2019)
- Add security to save files to prevent cheating (Added 11/12/2019)
- Add reactions to combat (1x per encounter), i.e. Counterspell, evasion, dodge, etc.
- Transition game to more "Rogue-lite" style, 3 floors, faster leveling, <s> and permanent upgrades between runs</s> (Completed 6/21/2020) (Added 6/21/2020)
- Flesh out skill trees and add more (Added 6/21/2020)
- Add custom username/generator (Added 6/21/2020)

## Update (7/2/2019)
- Added Armor and Weapon Durablitity
- Added Armor Rating field
- Can have a total of 2 weapons, 1 Helmet, 1 Chest Piece, and 1 Leg (Note: Weapons are selected at time of attack --- dual wield skill in progress)
- Added Armor Absorption with scaling (# of armor pieces (Max 3) * armor rating of each piece (1 - 10) * player level)
- Fixed an issue with weapons and armor sharing damage
- Fixed weapon and item usage (in progress before)

## Update (7/3/2019)
- Added Bonfire event frame (marker and flow, no functionality yet)
- Added Real Time Map that tracks events and rooms via Map Markers
- Added a Stairs event to traverse deeper in the dungeon
- Added a "Stuck" event if the map doesn't generate a stairs event (rare, known issue)
- Cleaned up print out minorly (deleted some print statements)

## Update (7/15/2019)
- Added Bonfire event functionality: Rest (Recover HP, or gain temporary if HP is at max (Overheal)), Mediate (Gain Experience), Repair Equipment
- Updated level system thresholds
- Major Updates to print outs ---> Deletions, Rewrites, and Formatted print out methods for equipment, items, and skills
- Buffed exp gained from minions to align with exp path updates
- Updated Health and Mana on Level Up (+30 Hp, +10 exp) (work in progress)
- Health and Mana is now restored on level up

## Update (11/12/2019)
- Straying away from traditional rogue-lites I have added a save feature that restores player states as well as dungeon state which mirrors the map layout

## Update (6/21/2020)
- Added Permanent Upgrades between runs so players have an incentive to keep playing (in progress, needs testing and furthur dev but pipeline is there)
- Removed attempt at PyGame, didn't fit the theme of "Zork-esc"
- Minor text output changes
- Dying now deletes your dungeon, map, and player, but keeps your Purchased Upgrades
- Upgrades are Optional
- Updated hint menu to reflect new changes
