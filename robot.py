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
    def __init__(self, robot_radius = 5, robot_position=[400, 300], color=(0, 0, 255), numPoints=200, center_angle=0):
        self.robot_radius = robot_radius
        self.robot_position = robot_position
        self.color = color
        self.robot_verts = makeCircle(numPoints=numPoints, color=color, circle_center=self.robot_position, radius=self.robot_radius)
        self.numPoints = numPoints

        self.sensors = []
        self.center_angle = center_angle

    def draw(self):
        circle_vertices = pyglet.graphics.vertex_list(self.numPoints, ('v2f', self.robot_verts),
        ('c3B', self.color * self.numPoints))

        circle_vertices.draw(pyglet.gl.GL_LINE_LOOP)

        for sensor_id, sensor in enumerate(self.sensors):
            self.sensors[sensor_id].draw()

    def add_sensors(self, sensor_object):
        self.sensors.append(sensor_object)

    def update_robot_pos(self):
        self.robot_verts = makeCircle(numPoints=self.numPoints, color=self.color, circle_center=self.robot_position, radius=self.robot_radius)
        for i in range(len(self.sensors)):
            self.sensors[i].set_pos(self.robot_position)
            self.sensors[i].set_center_angle(self.center_angle)


class Ball:
    def __init__(self, ball_radius = 5, ball_position=[200, 200], color=(0, 0, 255), numPoints=200, center_angle=0):
        self.ball_radius = ball_radius
        self.ball_position = ball_position
        self.color = color
        self.ball_verts = makeCircle(numPoints=numPoints, color=color, circle_center=self.ball_position, radius=self.ball_radius)
        self.numPoints = numPoints
        self.center_angle = center_angle

    def draw(self):
        circle_vertices = pyglet.graphics.vertex_list(self.numPoints, ('v2f', self.ball_verts),
        ('c3B', self.color * self.numPoints))

        circle_vertices.draw(pyglet.gl.GL_LINE_LOOP)

    # def update_ball_pos(self, ball_position, center_angle):
    #     self.center_angle = center_angle
    #     self.ball_position = ball_position
    #     self.ball_verts = makeCircle(numPoints=self.numPoints, color=self.color, circle_center=self.ball_position, radius=self.ball_radius)
