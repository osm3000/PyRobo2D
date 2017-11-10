import pyglet
import numpy as np
class Sensors:
    def __init__(self, sensor_coverage=180, num_rays=9, color=(0, 0, 255), sensor_range=60, center_angle=0):
        self.sensor_range = sensor_range
        self.sensor_coverage = sensor_coverage
        self.num_rays = num_rays
        self.center_angle = center_angle
        self.color = color

        self.rotation_angle = self.initialize_sensor_angles(self.center_angle, self.num_rays, self.sensor_coverage)
        self.sensor_pos = [400, 300]

        self.current_sensor_rays = []
        self.sensor_ranges = [-1 for i in range(num_rays)]

    def initialize_sensor_angles(self, center_angle, num_rays, sensor_coverage):
        return np.linspace(center_angle-0.5*sensor_coverage, center_angle+0.5*sensor_coverage, num_rays)

    def set_pos(self, new_pos):
        self.sensor_pos = new_pos

    def set_center_angle(self, center_position):
        self.center_angle = center_position
        self.rotation_angle = self.initialize_sensor_angles(self.center_angle, self.num_rays, self.sensor_coverage)

    def update_sensor_rays(self):
        self.current_sensor_rays = []
        for angle in self.rotation_angle:
            x1 = self.sensor_range * np.cos(np.deg2rad(angle))
            y1 = self.sensor_range * np.sin(np.deg2rad(angle))

            x1 += self.sensor_pos[0]
            y1 += self.sensor_pos[1]

            self.current_sensor_rays.append([self.sensor_pos[0], self.sensor_pos[1], x1, y1])
        return self.current_sensor_rays
    def draw(self):
        self.current_sensor_rays = self.update_sensor_rays()
        for ray in self.current_sensor_rays:
            pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2f', ray), ('c3B', self.color * 2) )

    def set_sensor_range(self, sensor_ranges):
        assert len(sensor_ranges) == self.num_rays
