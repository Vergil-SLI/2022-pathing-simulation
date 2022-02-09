import pygame, sys
import field
from wavepoint import Wavepoint

pygame.init()


# FPS cap
frame_rate = pygame.time.Clock()
FPS = 15

# variables
loop_end = False
orange = [50, 250, 50]
window = field.Field(714, 359)
wavepoint_List = []
wavepoint_index = 0


# simulation loop, press _____ to exit
while not loop_end:
    # Idk what this do exactly but it keeps my code from crashing so.....
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    # set FPS
    frame_rate.tick(FPS)


    # detect computer inputs
    left_click = pygame.mouse.get_pressed()[0]  # bool for whether left click is pressed
    right_click = pygame.mouse.get_pressed()[2]
    escape = pygame.key.get_pressed()[27] # bool for whether ESC is pressed


    # check if we should make a wavepoint
    if left_click:
        point = Wavepoint(orange, window, FPS, wavepoint_index)
        wavepoint_List.append(point)


        # remove the first "wavepoint" which is set to be 0 at the start
        if wavepoint_List[0] == 0:
            wavepoint_List.remove(0)


        wavepoint_List[wavepoint_index].setPoint()
        wavepoint_index += 1


        # draw out all the wavepoints
        for wavepoint in wavepoint_List:
            wavepoint.draw_point()


    if

    # check if the simulation is done
    if escape:
        loop_end = not loop_end



for wavepoint in wavepoint_List:
    print(wavepoint.return_position())
