import numpy as np
import pyglet
from collision_detection import *
from sensors import *
from pyglet.window import key
from robot import *
from robot_status import *
from agents import *
from game_logic import *
class Window(pyglet.window.Window):
    def __init__(self, width=600, height=600, visible=True):
        """
        This is the class constructor
        """
        super(Window, self).__init__(width, height, visible=visible) #It takes the size of the window

        self.keys = dict(up=None, left=None, right=None, down=None)

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

        # self.robot_agent = AgentRandom()
        self.robot_agent = None
        self.game_logic_instance = Collect_Ball_Simple()

    def add_objects_to_environment(self, object_instance):
        self.environment_objects.append(object_instance)

    def on_draw(self):
        """
        Inherited method. We need to override it in order to create
        a drawing
        """
        if self.visible:
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

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = False
        elif symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False
        elif symbol == key.DOWN:
            self.keys['down'] = False

    def update(self, dt):
        # Read agent status
        if self.robot_agent != None: # If an agent is set, then override the keyboard
            self.keys = self.robot_agent.get_next_move()

        step_size = 5
        if self.keys["up"]:
            for i in range(len(self.robots)):
                self.robots[i].circle_position_temp[1] = self.robots[i].circle_position[1] + step_size * np.sin(np.deg2rad(self.robots[i].center_angle))
                self.robots[i].circle_position_temp[0] = self.robots[i].circle_position[0] + step_size * np.cos(np.deg2rad(self.robots[i].center_angle))

        elif self.keys["down"]:
            for i in range(len(self.robots)):
                self.robots[i].circle_position_temp[1] = self.robots[i].circle_position[1] - step_size * np.sin(np.deg2rad(self.robots[i].center_angle))
                self.robots[i].circle_position_temp[0] = self.robots[i].circle_position[0] - step_size * np.cos(np.deg2rad(self.robots[i].center_angle))

        elif self.keys["left"]:
            for i in range(len(self.robots)):
                self.robots[i].center_angle += 5

        elif self.keys["right"]:
            for i in range(len(self.robots)):
                self.robots[i].center_angle -= 5

        for i in range(len(self.robots)):
            collision_detection_dic = collision_detection(self.robots[i], self.env_objects)
            if True not in list(collision_detection_dic.values()): # Check if there is any collision
                self.robots[i].circle_position[1] = self.robots[i].circle_position_temp[1]
                self.robots[i].circle_position[0] = self.robots[i].circle_position_temp[0]

        # Update robot position
        for i in range(len(self.robots)):
            self.robots[i].update_robot_pos()

        # Perform sensor_readings
        sensors_recording = []
        for i in range(len(self.robots)):
            sensors_recording = sensor_range_detection(self.robots[i], self.env_objects)

            for j in range(len(sensors_recording)): # Remove the extra sensory reading --> What is that??? --> This is just to correct the extra reading
            # resulting from the fact that the sensors are coming from the center of the robot
                if sensors_recording[j] != -1:
                    sensors_recording[j] -= self.robots[i].circle_radius
            if isinstance(self.robot_status, RobotStatus): # TODO: This is suitable for one robot right now
                self.robot_status.robot_position.append(self.robots[i].circle_position)
                self.robot_status.robot_rotation.append(self.robots[i].center_angle)
                self.robot_status.robot_sensors_readings.append(sensors_recording)
                self.robot_status.collisions.append(collision_detection_dic)

            print (self.robot_status.get_robot_status())

        # Update the game logic
        game_over, game_score = self.game_logic_instance.update_fsm(self.robot_status)
        self.robot_status.game_over = game_over
        self.robot_status.game_score = game_score
        # print ("Game FSM: ", self.game_logic_instance.game_fsm)
        # print ("Game Over: ", self.robot_status.game_over)
        # print ("Game Over: ", self.robot_status.game_score)

    def add_env_objects(self, env_object_object):
        self.env_objects.append(env_object_object)

    def add_robot(self, robot_object):
        self.robots.append(robot_object)

    def set_agent(self, agent_object):
        self.robot_agent = robot_object
