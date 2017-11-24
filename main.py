import window
from walls import *
import robot
from sensors import *
from agents import *
# def update(dt):
#     window.update()
if __name__ == "__main__":
    my_robot = robot.Robot(circle_radius=20, name="lovely_robot", color=(0, 0, 0))
    my_robot.add_sensors(Sensors(sensor_coverage=180, num_rays=9, color=(0, 0, 255), sensor_range=60, center_angle=0, name="sensor_0"))
    my_robot.add_sensors(Sensors(sensor_coverage=110, num_rays=4, color=(255, 0, 0), sensor_range=60, center_angle=0, name="sensor_1"))

    width, heigth = 800, 800
    window = window.Window(width=width, height=heigth)
    window.add_env_objects(Wall(color=(0, 0, 255), wall_coordinates=[1, 1, 1, heigth-1], name="wall_1"))
    window.add_env_objects(Wall(color=(0, 0, 255), wall_coordinates=[1, 1, width-1, 1], name="wall_2"))
    window.add_env_objects(Wall(color=(0, 0, 255), wall_coordinates=[width-1, 1, width-1, heigth-1], name="wall_3"))
    window.add_env_objects(Wall(color=(0, 0, 255), wall_coordinates=[1, heigth-1, width-1, heigth-1], name="wall_4"))

    # window.add_env_objects(Wall(color=(0, 0, 255), wall_coordinates=[1, 1, 1, heigth-1], name="wall_8"))
    # window.add_env_objects(Wall(color=(0, 0, 255), wall_coordinates=[1, 1, width-1, 1], name="wall_5"))
    # window.add_env_objects(Wall(color=(0, 0, 255), wall_coordinates=[width-1, 1, width-1, heigth-1], name="wall_6"))
    # window.add_env_objects(Wall(color=(0, 0, 255), wall_coordinates=[1, heigth-1, width-1, heigth-1], name="wall_7"))

    # window.add_env_objects(robot.Ball(circle_radius=10, color=(255, 0, 0), name="ball_0", circle_position=[400, 400]))
    # window.add_env_objects(robot.Ball(circle_radius=10, color=(255, 0, 0), name="ball_1", circle_position=[300, 300]))
    # window.add_env_objects(robot.Ball(circle_radius=10, color=(255, 0, 0), name="ball_2", circle_position=[200, 200]))
    # window.add_env_objects(robot.Ball(circle_radius=10, color=(255, 0, 0), name="ball_3", circle_position=[100, 100]))
    # window.add_env_objects(robot.Ball(circle_radius=40, color=(0, 0, 255), name="basket", circle_position=[500, 500]))
    window.add_robot(my_robot)
    pyglet.app.run()
