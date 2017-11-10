import pyglet
import numpy as np
from math import *
def makeCircle(numPoints=200, color=(200, 100, 50)):
    verts = []
    for i in range(numPoints):
        angle = radians(float(i)/numPoints * 360.0)
        x = 100*cos(angle) + 300
        y = 100*sin(angle) + 200
        verts += [x,y]
    return verts

class Robot:
    def __init__(self, robot_radius = 10, robot_position=[200, 200], color=(0, 0, 255), numPoints=200):
        self.robot_radius = robot_radius
        self.robot_position = robot_position
        self.color = color
        self.robot_verts = makeCircle(numPoints=numPoints, color=color)
        self.numPoints = numPoints

    def draw(self):
        circle_vertices = pyglet.graphics.vertex_list(self.numPoints, ('v2f', self.robot_verts),
        ('c3B', self.color * self.numPoints))

        circle_vertices.draw(pyglet.gl.GL_LINE_LOOP)
