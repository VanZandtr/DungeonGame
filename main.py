import math
import random
import pygame
import Dungeon_Main
from pygame import mixer
from pygame.locals import *
import os
import sys

# Intialize the pygame
pygame.init()

#dispay dimensions
display_width = 800
display_height = 600
# create the screen
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Background
#background = pygame.image.load('background.png')

# Sound
#mixer.music.load("background.wav")
#mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Dungeon Game")
#icon = pygame.image.load('ufo.png')
#pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('wizard.png')
playerX = 370
playerY = 480
#playerX_change = 0

black = (0,0,0)
white = (255, 255, 255)
red = (200,0,0)
green = (0, 200, 0)
bright_red = (255,0,0)
bright_green = (0,255,0)
block_color = (53, 115, 255)


#clock
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#x: The x location of the top left coordinate of the button box. 
#y: The y location of the top left coordinate of the button box. 
#w: Button width. h: Button height. 
#ic: Inactive color (when a mouse is not hovering). 
#ac: Active color (when a mouse is hovering). 
#action: function passed to run on click
def button(msg,x,y,w,h,ic,ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def get_key():
    while 1:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            return event.key
        else:
            pass
    
def make_display_box(screen, message, left, top, width, height, background_color, outline_color, message_color):
    fontobject = pygame.font.Font(None, 18)
    
    #Background
    pygame.draw.rect(screen, background_color, [left, top, width, height], 0)
    #Outline
    pygame.draw.rect(screen, outline_color, [left - 2, top - 2, width + 4, height + 4], 1)
    if len(message) != 0:
        i = 0
        for lines in message.splitlines():
            screen.blit(fontobject.render(lines, 1, message_color), [left, top + (i*12)])
            i+=1
    pygame.display.flip()
        
    

def ask(screen, question):
    "ask(screen, question) -> answer"
    pygame.font.init()
    current_string = []
    
    make_display_box(screen, (question + ": " + "".join(current_string)), 
                     ((screen.get_width() / 2) - display_width/4), 10, 400, 40, 
                     black, red, white)
    
    while 1:
        inkey = get_key()
        if inkey == pygame.K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == pygame.K_RETURN:
                break
        elif inkey == pygame.K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
        make_display_box(screen, (question + ": " + "".join(current_string)), 
                     ((screen.get_width() / 2) - display_width/4), 10, 400, 40, 
                     black, red, white)
    return "".join(current_string)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Dungeon Game", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("Start", 150, 450, 100 , 50, green, bright_green, game_loop)
        button("Quit", 550, 450, 100 , 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(15)
        
def game_loop():
    #clear screen
    gameDisplay.fill(white)
    
    
    #longer history of text if wanted
    history = []
    
    ret = Dungeon_Main.hint()
    make_display_box(gameDisplay, ret, ((display_width/ 2) - 250), 
                     350, 500, 200, black, red, white)
    
    while True:
        command = ask(gameDisplay, "What would you like to do? ")        
        quit_flag, ret = Dungeon_Main.main_loop(command)
    
        history.append(ret)
        history.append('\n')
        
        make_display_box(gameDisplay, ret, ((display_width/ 2) - 250), 
                     350, 500, 200, black, red, white)
        
        if quit_flag == True:
            break
    
def load_game():
    print("load_game to be implmented")
    
def quit_game():
    pygame.quit()        
###############################################################################
game_intro()
pygame.quit()
