import window
from walls import *
import robot
from sensors import *
from agents import *
# def update(dt):
#     window.update()
if __name__ == "__main__":
    print ("oh la laa")
    my_robot = robot.Robot(circle_radius=20)
    # ball = robot.Ball(ball_radius =40, color=(255, 255, 0))
    my_robot.add_sensors(Sensors(sensor_coverage=180, num_rays=9, color=(0, 0, 255), sensor_range=60, center_angle=0))
    my_robot.add_sensors(Sensors(sensor_coverage=110, num_rays=4, color=(255, 0, 0), sensor_range=60, center_angle=0))
    window = window.Window()
    # pyglet.clock.schedule_interval(window.update, 1/120.0)
    # window.add_env_objects(Wall(color=(0, 0, 255), wall_coordinates=[300, 0, 300, 600]))
    window.add_env_objects(Wall(color=(0, 0, 255), wall_coordinates=[300, 0, 300, 200]))
    window.add_env_objects(Wall(color=(0, 0, 255), wall_coordinates=[0, 200, 300, 200]))
    window.add_env_objects(Wall(color=(0, 0, 255), wall_coordinates=[300, 400, 300, 600]))
    window.add_env_objects(Wall(color=(255, 0, 0), wall_coordinates=[100, 0, 100, 600]))
    # window.add_env_objects(robot.Ball(circle_radius=40, color=(255, 0, 0)))
    window.add_robot(my_robot)
    pyglet.app.run()
