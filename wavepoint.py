import pygame
import sys

class Wavepoint():


    def __init__(self, color, field, FPS, index):
        self.color = color
        self.window = field
        self.FPS = FPS
        self.center = [0, 0]
        self.index = index


    def setPoint(self):
        end_loop = False
        coordinate = [0, 0]

        while not end_loop:

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()


            #draw circles that follow the mouse
            coordinate = pygame.mouse.get_pos()
            pygame.draw.circle(self.window.return_screen(), self.color, coordinate, 5)
            self.window.background_refresh()

            #check if the variables updated
            end_loop = pygame.key.get_pressed()[13]
            pygame.time.Clock().tick(self.FPS)

        #update the class variables
        self.center = coordinate
        self.window.clear()



    def draw_point(self):
        pygame.draw.circle(self.window.return_screen(), self.color, self.center, 5)
        self.window.background_refresh()


    def return_position(self):
        return self.center


