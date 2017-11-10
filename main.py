import window
from walls import *
# def update(dt):
#     window.update()
if __name__ == "__main__":
    print ("oh la laa")
    window = window.Window()
    # pyglet.clock.schedule_interval(window.update, 1/120.0)
    window.add_walls(Wall(color=(0, 0, 255), wall_coordinates=[300, 0, 300, 600]))
    window.add_walls(Wall(color=(255, 0, 0), wall_coordinates=[100, 0, 100, 600]))
    pyglet.app.run()
