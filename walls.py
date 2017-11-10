import pyglet
class Wall:
    def __init__(self, color=(0, 0, 255), wall_coordinates=[300, 0, 300, 600]):
        self.color = color
        self.wall_coordinates = wall_coordinates
    def draw(self):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', self.wall_coordinates), ('c3B', self.color * 2))
