from walls import *
import robot
from sensors import *
from agents import *
def basic_collectball_map_static(width=600, height=600):
    my_robot = robot.Robot(circle_radius=20, name="lovely_robot", color=(0, 0, 0), circle_position=[200, 200])
    my_robot.add_sensors(Sensors(sensor_coverage=180, num_rays=9, color=(0, 0, 255), sensor_range=60, center_angle=0, name="sensor_0"))
    my_robot.add_sensors(Sensors(sensor_coverage=110, num_rays=4, color=(255, 0, 0), sensor_range=60, center_angle=0, name="sensor_1"))

    env_objects = []

    # Adding the walls
    env_objects.append(Wall(color=(0, 0, 255), wall_coordinates=[1, 1, 1, height-1], name="wall_1"))
    env_objects.append(Wall(color=(0, 0, 255), wall_coordinates=[1, 1, width-1, 1], name="wall_2"))
    env_objects.append(Wall(color=(0, 0, 255), wall_coordinates=[width-1, 1, width-1, height-1], name="wall_3"))
    env_objects.append(Wall(color=(0, 0, 255), wall_coordinates=[1, height-1, width-1, height-1], name="wall_4"))
    #
    env_objects.append(Wall(color=(0, 0, 255), wall_coordinates=[int(width/3), 1, int(width/2), int(2*height/8)], name="wall_5"))
    env_objects.append(Wall(color=(0, 0, 255), wall_coordinates=[int(width/2), int(3*height/8), int(width/2), int(5*height/8)], name="wall_6"))
    env_objects.append(Wall(color=(0, 0, 255), wall_coordinates=[int(width/2), int(6*height/8), int(width/2), int(8*height/8)], name="wall_7"))
    #
    env_objects.append(Wall(color=(0, 0, 255), wall_coordinates=[int(6*width/8), int(height/2), int(8*width/8), int(height/2)], name="wall_8"))
    env_objects.append(Wall(color=(0, 0, 255), wall_coordinates=[1, int(height/2), int(2*width/8), int(height/2)], name="wall_9"))
    env_objects.append(Wall(color=(0, 0, 255), wall_coordinates=[int(3*width/8), int(height/2), int(5*width/8), int(height/2)], name="wall_10"))

    # Adding the balls
    env_objects.append(robot.Ball(circle_radius=10, color=(255, 0, 0), name="ball_0", circle_position=[400, 400]))
    env_objects.append(robot.Ball(circle_radius=10, color=(255, 0, 0), name="ball_1", circle_position=[300, 300]))
    env_objects.append(robot.Ball(circle_radius=10, color=(255, 0, 0), name="ball_2", circle_position=[200, 200]))
    env_objects.append(robot.Ball(circle_radius=10, color=(255, 0, 0), name="ball_3", circle_position=[100, 100]))
    env_objects.append(robot.Ball(circle_radius=40, color=(0, 0, 255), name="basket", circle_position=[500, 500]))

    return my_robot, env_objects
