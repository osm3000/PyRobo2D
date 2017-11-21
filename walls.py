import pyglet
class Wall:
    def __init__(self, color=(0, 0, 255), wall_coordinates=[300, 0, 300, 600]):
        self.color = color
        self.wall_coordinates = wall_coordinates[:]
        self.collision_enabled = True

        # This is due to the problem I've in the collision detection - Dirty solution
        if self.wall_coordinates[0] == self.wall_coordinates[2]:
            self.wall_coordinates[2] += 1
        if self.wall_coordinates[1] == self.wall_coordinates[3]:
            self.wall_coordinates[3] += 1
    def draw(self):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', self.wall_coordinates), ('c3B', self.color * 2))
