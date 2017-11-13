import numpy as np
import pyglet
from collision_detection import *
from sensors import *
from pyglet.window import key
from robot import *
from robot_status import *
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

        self.env_objects = []
        self.robots = []

        self.environment_objects = []
        if visible:
            pyglet.clock.schedule_interval(self.update, 1/120.0)

        self.robot_status = RobotStatus()

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

        # Build env_objects
        for env_object_id, env_object in enumerate(self.env_objects):
            self.env_objects[env_object_id].draw()

        for robot_id, robot in enumerate(self.robots):
            self.robots[robot_id].draw()

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
        step_size = 1
        if self.keys["up"]:
            for i in range(len(self.robots)):
                self.robots[i].robot_position[1] += step_size * np.sin(np.deg2rad(self.robots[i].center_angle))
                self.robots[i].robot_position[0] += step_size * np.cos(np.deg2rad(self.robots[i].center_angle))
        elif self.keys["down"]:
            for i in range(len(self.robots)):
                self.robots[i].robot_position[1] -= step_size * np.sin(np.deg2rad(self.robots[i].center_angle))
                self.robots[i].robot_position[0] -= step_size * np.cos(np.deg2rad(self.robots[i].center_angle))

        elif self.keys["left"]:
            for i in range(len(self.robots)):
                self.robots[i].center_angle += 5

                # Quick reset of the angle to the range of 0-360 --> Doesn't affect the performance
                if self.robots[i].center_angle > 360:
                    self.robots[i].center_angle -= 360
                if self.robots[i].center_angle < 0:
                    self.robots[i].center_angle += 360
        elif self.keys["right"]:
            for i in range(len(self.robots)):
                self.robots[i].center_angle -= 5

                # Quick reset of the angle to the range of 0-360 --> Doesn't affect the performance
                if self.robots[i].center_angle > 360:
                    self.robots[i].center_angle -= 360
                if self.robots[i].center_angle < 0:
                    self.robots[i].center_angle += 360

        # Update robot position
        for i in range(len(self.robots)):
            self.robots[i].update_robot_pos()

        # Perform collision detection
        sensors_recording = []
        if len(self.robots) > 0:
            for i in range(len(self.robots)):
                for sensor_id, sensor in enumerate(self.robots[i].sensors):
                    sensors_recording += sensor_range_detection(sensor, self.env_objects)

                if isinstance(self.robot_status, RobotStatus): # TODO: This is suitable for one robot right now
                    self.robot_status(RobotPosition=self.robots[i].robot_position, RobotRotation = self.robots[i].center_angle,
                    RobotSensorsReadings = sensors_recording)
            print (self.robot_status)

    def add_env_objects(self, env_object_object):
        self.env_objects.append(env_object_object)

    def add_robot(self, robot_object):
        self.robots.append(robot_object)
