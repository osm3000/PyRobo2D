import pyglet
import numpy as np
from math import *
def makeCircle(numPoints=200, color=(200, 100, 50), circle_center=(300, 200), radius=100):
    verts = []
    for i in range(numPoints):
        angle = radians(float(i)/numPoints * 360.0)
        x = radius*cos(angle) + circle_center[0]
        y = radius*sin(angle) + circle_center[1]
        verts += [x,y]
    return verts

class Robot:
    def __init__(self, circle_radius = 5, circle_position=[400, 300], color=(0, 0, 255), numPoints=200, center_angle=0):
        self.circle_radius = circle_radius
        self.circle_position = circle_position[:]
        self.center_angle = center_angle
        self.circle_position_temp = circle_position[:]
        self.center_angle_temp = center_angle
        self.color = color
        self.robot_verts = makeCircle(numPoints=numPoints, color=color, circle_center=self.circle_position, radius=self.circle_radius)
        self.numPoints = numPoints

        self.sensors = []
        self.collision_enabled = True

    def draw(self):
        circle_vertices = pyglet.graphics.vertex_list(self.numPoints, ('v2f', self.robot_verts),
        ('c3B', self.color * self.numPoints))

        circle_vertices.draw(pyglet.gl.GL_LINE_LOOP)

        for sensor_id, sensor in enumerate(self.sensors):
            self.sensors[sensor_id].draw()

    def add_sensors(self, sensor_object):
        self.sensors.append(sensor_object)

    def update_robot_pos(self):
        self.robot_verts = makeCircle(numPoints=self.numPoints, color=self.color, circle_center=self.circle_position, radius=self.circle_radius)
        for i in range(len(self.sensors)):
            self.sensors[i].set_pos(self.circle_position)
            self.sensors[i].set_center_angle(self.center_angle)
            self.sensors[i].update_sensor_rays()


class Ball:
    def __init__(self, circle_radius = 5, circle_position=[200, 200], color=(0, 0, 255), numPoints=200, center_angle=0):
        self.circle_radius = circle_radius
        self.circle_position = circle_position
        self.color = color
        self.ball_verts = makeCircle(numPoints=numPoints, color=color, circle_center=self.circle_position, radius=self.circle_radius)
        self.numPoints = numPoints
        self.center_angle = center_angle

        self.collision_enabled = True

    def draw(self):
        circle_vertices = pyglet.graphics.vertex_list(self.numPoints, ('v2f', self.ball_verts),
        ('c3B', self.color * self.numPoints))

        circle_vertices.draw(pyglet.gl.GL_LINE_LOOP)

    # def update_ball_pos(self, circle_position, center_angle):
    #     self.center_angle = center_angle
    #     self.circle_position = circle_position
    #     self.ball_verts = makeCircle(numPoints=self.numPoints, color=self.color, circle_center=self.circle_position, radius=self.circle_radius)
