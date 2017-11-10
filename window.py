import numpy as np
import pyglet
from collision_detection import *
from sensors import *
from pyglet.window import key
from robot import *
class Window(pyglet.window.Window):
    def __init__(self, width=600, height=600, visible=True):
        """
        This is the class constructor
        """
        super(Window, self).__init__(width, height, visible=visible) #It takes the size of the window
        self.init_square = (300, 300,
                       300, 350,
                       350, 300,
                       350, 350)
        self.position = dict(x1=300, y1=300, x2=300, y2=350, x3=350, y3=300,
                             x4=350, y4=350)
        self.keys = dict(up=None, left=None, right=None, down=None, rotate_right=None, rotate_left=None)

        self.width = width
        self.height = height

        self.robot_position = [400, 300]

        self.center_angle = 0
        self.sensors = []
        self.sensors.append(Sensors(sensor_coverage=180, num_rays=9, color=(0, 0, 255), sensor_range=60, center_angle=self.center_angle))
        self.sensors.append(Sensors(sensor_coverage=110, num_rays=4, color=(255, 0, 0), sensor_range=60, center_angle=self.center_angle))

        self.walls = []
        self.robot = Robot()

        self.environment_objects = []
        if visible:
            pyglet.clock.schedule_interval(self.update, 1/120.0)

    def add_objects_to_environment(self, object_instance):
        self.environment_objects.append(object_instance)

    def on_draw(self):
        """
        Inherited method. We need to override it in order to create
        a drawing
        """
        self.clear() # This will clear the window
        # Make the background white
        pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                     [0, 1, 2, 1, 2, 3],
                                     ('v2i', (0, 0,
                                            self.width, 0,
                                            0, self.height,
                                            self.width, self.height)),
                                     ('c3B', (255, 255, 255) * 4))
        for sensor_id, sensor in enumerate(self.sensors):
            self.sensors[sensor_id].draw()
        # Build walls
        for wall_id, wall in enumerate(self.walls):
            self.walls[wall_id].draw()

        self.robot.draw()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = True
        elif symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True
        elif symbol == key.DOWN:
            self.keys['down'] = True

        elif symbol == key.A:
            self.keys['rotate_left'] = True
        elif symbol == key.D:
            self.keys['rotate_right'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = False
        elif symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False
        elif symbol == key.DOWN:
            self.keys['down'] = False

        elif symbol == key.A:
            self.keys['rotate_left'] = False
        elif symbol == key.D:
            self.keys['rotate_right'] = False

    def update(self, dt):
        # print (self.center_angle)
        step_size = 1
        if self.keys["up"]:
            self.robot_position[1] += step_size * np.sin(np.deg2rad(self.center_angle))
            self.robot_position[0] += step_size * np.cos(np.deg2rad(self.center_angle))

        elif self.keys["down"]:
            self.robot_position[1] -= step_size * np.sin(np.deg2rad(self.center_angle))
            self.robot_position[0] -= step_size * np.cos(np.deg2rad(self.center_angle))

        elif self.keys["left"]:
            self.center_angle += 5
        elif self.keys["right"]:
            self.center_angle -= 5

        for i in range(len(self.sensors)):
            self.sensors[i].set_pos(self.robot_position)
            self.sensors[i].set_center_angle(self.center_angle)

        for sensor_id, sensor in enumerate(self.sensors):
            sensor_range_detection(sensor, self.walls)

    def add_walls(self, wall_object):
        self.walls.append(wall_object)
