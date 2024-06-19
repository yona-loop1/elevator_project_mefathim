"""The order of the files is as follows:
1. CONFIG; 2. FLOOR_CLASS; 3. ELEVATOR_CLASS; 4. BUILDING_CLASS; 5. MAIN;
each file imports data from the previous one.
the main file draws the screen to the game, and calls the building and elevator functions in loop."""
import BUILDING_CLASS
from BUILDING_CLASS import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), vsync = 1)
Building = BUILDING_CLASS.Building()

run = True
while run:
    screen.fill(SCREEN_BACKGROUND)
    Building.update_building()
    Building.draw_building(screen)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            Building.ordering_elevator(x, y)

    pygame.display.update()

pygame.quit()