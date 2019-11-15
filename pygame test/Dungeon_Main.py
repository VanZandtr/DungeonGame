# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:36:40 2019

@author: rlv220
"""


def main_loop(command):
    quit_flag = False
    if command in ['q','Q','exit','Exit','Quit','quit']:
        print("quitting")
        print()
        quit_flag = True
        
    elif command in ['north', 'North', 'move North', 'Move North', 'move north', 'Move north']:
        print()
        print("The adventurer moves north.")
       
        
    elif command in ['south', 'South', 'move South', 'Move South', 'move south', 'Move south']:
        print()
        print("The adventurer moves south.")
        
    elif command in ['east', 'East', 'move East', 'Move East', 'move east', 'Move east']:
        print()
        print("The adventurer moves east.")
        
    elif command in ['west', 'West', 'move West', 'Move West', 'move west', 'Move west']:
        print()
        print("The adventurer moves west.")
        
    elif command in ['I', 'i', 'Inventory', 'inventory']:
        print()
        print("----------Inventory----------")
    
    elif command in ['U','u','unequip', 'Unequip']:
        print()
        print("Unequipping")         
        
    elif command in ['E','e','equip', 'Equip']:
        print()
        print("Equiping")
                
    elif command in ['S', 's', 'Skills', 'skills']:
        print()
        print("----------Skills----------")
    
    elif command in ['H','h','hint', 'Hint']:
        print()
        print("hint")
    
    elif command in ['Stuck', 'stuck']:
        print()
        print("HAVE THIS CHECK IF NO ROOM HAD THE STAIRS EVENT FIRST!")
        
    elif command in ['SAV', 'sav', 'Sav']:
        print()
        print("The adventurer has saved his progression")
        
    else:
        print()
        print("I am unsure what the adventurer wants.")
    return quit_flag