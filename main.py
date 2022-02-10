import pygame, sys
import field, conversion
from wavepoint import Wavepoint
from wpimath import trajectory, geometry

pygame.init()

# FPS cap
FPS = 30
g1 = (255, 100, 100)  # gradiant starting color
g2 = (100, 100, 255)  # gradiant ending color
orange = [50, 250, 50]

# variables
loop_end = False
window = field.Field(1227, 623)
wavepoint_List = []
wavepoint_index = 0
wavepoint_selection = 0
frame_rate = pygame.time.Clock()
convert = conversion.Conversion(1227, 623, 16.4592, 8.2296)
path_generator = trajectory.TrajectoryGenerator
point_list = []


# change the point color
def gradient(x: float) -> tuple[int, int, int]:
    def interp(idx):
        return x * g2[idx] + (1 - x) * g1[idx]

    return interp(0), interp(1), interp(2)


# simulation loop, press _____ to exit
while not loop_end:
    # Idk what this do exactly but it keeps my code from crashing so.....
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # set FPS
    frame_rate.tick(FPS)

    # detect computer inputs
    escape = pygame.key.get_pressed()[27]  # exit the program
    left_click = pygame.mouse.get_pressed()[0]  # start placing
    right_click = pygame.mouse.get_pressed()[2]  # display the current selection index
    middle_click = pygame.mouse.get_pressed()[1]  # change position of the selection index dot
    up_arrow = pygame.key.get_pressed()[1073741906]  # increase selection index
    down_arrow = pygame.key.get_pressed()[1073741905]  # decrease selection index
    backspace = pygame.key.get_pressed()[8]  # delete a point

    # check if we should make a wavepoint
    if left_click:
        point = Wavepoint(gradient(wavepoint_index / 10), window, wavepoint_index)
        wavepoint_List.append(point)

        # remove the first "wavepoint" which is set to be 0 at the start
        if wavepoint_List[0] == 0:
            wavepoint_List.remove(0)

        wavepoint_List[wavepoint_index].setPoint()
        wavepoint_index += 1

        # draw out all the wavepoints
        for wavepoint in wavepoint_List:
            wavepoint.draw_point()

    elif middle_click:
        wavepoint_List[wavepoint_selection].setPoint()

        # draw out all the wavepoints
        for wavepoint in wavepoint_List:
            wavepoint.draw_point()

    elif right_click:
        print(wavepoint_selection)
    elif escape:
        loop_end = not loop_end
    elif backspace:
        wavepoint_List.remove(wavepoint_List[wavepoint_selection])
        wavepoint_index -= 1

        window.clear()
        # draw out all the wavepoints
        for wavepoint in wavepoint_List:
            wavepoint.draw_point()

        if wavepoint_selection > wavepoint_index:
            wavepoint_selection = wavepoint_index


    # change the current point selected
    if down_arrow and wavepoint_selection > 0:
        wavepoint_selection -= 1
    elif down_arrow and wavepoint_selection == 0:
        wavepoint_selection = wavepoint_index
    elif up_arrow and wavepoint_selection < wavepoint_index:
        wavepoint_selection += 1
    elif up_arrow and wavepoint_selection == wavepoint_index:
        wavepoint_selection = 0



    # generate trajectory - i have no idea if this works
    if wavepoint_index > 1:
        for wavepoints in wavepoint_List:
            point_list.append(geometry.Pose2d(convert.pixel_to_meter(wavepoints.return_position()[0]), convert.pixel_to_meter(wavepoints.return_position()[1]), 0))

        config = trajectory.TrajectoryConfig(6, 6)
        path = path_generator.generateTrajectory(point_list, config)

        point_list.clear()
        # time = 0
        # for time == 5:

        x_list = []
        y_list = []

        for i in range(int(path.totalTime())+1):
            for j in range(10):
                x_list.append(convert.meter_to_pixel(path.sample(i+0.1*j).pose.X()))
                y_list.append(convert.meter_to_pixel(path.sample(i + 0.1 * j).pose.Y()))

                if i != 0 or j != 0:
                    pygame.draw.line(window.return_screen(), 255, [x_list[i*10+j], y_list[i*10+j]], [x_list[i*10+j-1], y_list[i*10+j-1]], 5)
                    window.background_refresh()



# report the coordinate of all the points
for wavepoint in wavepoint_List:
    print('x = ', convert.pixel_to_meter(wavepoint.return_position()[0]), ' y = ', convert.pixel_to_meter(wavepoint.return_position()[1]))
