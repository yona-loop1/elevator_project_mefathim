import pygame
import time
import math
import random

# screen's size and color
SCREEN_WIDTH =  700
SCREEN_HEIGHT = 700
SCREEN_BACKGROUND = [200, 200, 200]

# building's size and color\image
BUILDING_POSITION_WIDTH = SCREEN_WIDTH//100*15
BUILDING_POSITION_HEIGHT = 0
BUILDING_BACKGROUND = 'reference files/bricks.jpg'

# floor's configuration
MAX_FLOORS = 26
MIN_FLOORS = 7
NUMBER_FLOORS = random.randint(MIN_FLOORS, MAX_FLOORS)
FLOOR_HEIGHT = SCREEN_HEIGHT//NUMBER_FLOORS
FLOOR_WIDTH = 4*FLOOR_HEIGHT

# line's configuration (which is drawn between two floors)
LINE_SPACE = 7
LINE_POSITION = LINE_SPACE//2
LINE_COLOR = [0, 0, 0]

# button's configuration (which he orderes an elevator)
BUTTON_WIDTH = FLOOR_WIDTH//6
BUTTON_HEIGHT = BUTTON_WIDTH
BUTTON_POSITION_X = BUILDING_POSITION_WIDTH + FLOOR_WIDTH//2 - BUTTON_WIDTH//2
BUTTON_POSITION_Y = (FLOOR_HEIGHT+LINE_SPACE)//2 - BUTTON_HEIGHT//2
TEXT_BUTTON_POSITION_X = BUTTON_POSITION_X + BUTTON_WIDTH//2
TEXT_BUTTON_POSITION_Y = BUTTON_POSITION_Y + BUTTON_HEIGHT//2
SIZE_TEXT_BUTTON = 70*BUTTON_HEIGHT//100
BUTTON_COLOR = [0, 180, 160]
BUTTONS_TEXT_COLOR = [0, 0, 0]
GREEN = [0, 255, 0]

# timer's configuration (which he show the elevator's arrival time)
TIMER_WIDTH = 33*FLOOR_WIDTH//100
TIMER_HEIGHT = 80*BUTTON_HEIGHT//100
TIMER_COLOR = [0, 255, 90]
TIMER_POSITION_X = BUILDING_POSITION_WIDTH + 2*FLOOR_WIDTH//3
TIMER_POSITION_Y = (FLOOR_HEIGHT+LINE_SPACE)//2 - TIMER_HEIGHT//2
TEXT_TIMER_POSITION_X = TIMER_POSITION_X + TIMER_WIDTH//2
TEXT_TIMER_POSITION_Y = TIMER_POSITION_Y + TIMER_HEIGHT//2
SIZE_TEXT_TIMER = 70*TIMER_HEIGHT//100

TEXT_FONT = 'reference files/arial.ttf'

# elevator's configuration
MAX_ELEVATORS = 5 if NUMBER_FLOORS > 9 else 4 if NUMBER_FLOORS == 9 else 3 if NUMBER_FLOORS == 8 else 2 
MIN_ELEVATORS = 2
NUMBER_ELEVATORS = random.randint(MIN_ELEVATORS, MAX_ELEVATORS)
ELEVATOR_H = FLOOR_HEIGHT - LINE_SPACE
ELEVATOR_W = ELEVATOR_H
ELEVATOR_IMAGE = 'reference files/elv.png'
ARRIVAL_SOUND = 'reference files/ding.mp3'
TIME_PASS_FLOOR = 0.5
TIME_STOP_FLOOR = 2

