import pygame

class Wavepoint():


    def __init__(self, color, field, index):
        self.color = color
        self.window = field
        self.center = [0, 0]
        self.index = index


    def setPoint(self):
        end_loop = False
        coordinate = [0, 0]

        #draw circles that follow the mouse
        while not end_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()


            coordinate = pygame.mouse.get_pos()
            pygame.draw.circle(self.window.return_screen(), self.color, coordinate, 5)
            self.window.background_refresh()

            if pygame.key.get_pressed()[13]:
                end_loop = True


        #update the class variables
        self.center = coordinate
        self.window.clear()



    def draw_point(self):
        pygame.draw.circle(self.window.return_screen(), self.color, self.center, 5)
        self.window.background_refresh()


    def return_position(self):
        return self.center


