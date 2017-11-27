"""
This is an experimental main fn, in order to test the game
"""
import window
from walls import *
import robot
from sensors import *
from agents import *
import maps

if __name__ == "__main__":
    print ("start.....")
    width, height = 600, 600
    window = window.Window(width=width, height=height, visible=False)
    # window = window.Window(width=width, height=height)

    my_robot, env_objects = maps.basic_collectball_map_static(width=width, height=height)
    window.add_robot(my_robot)
    for item in env_objects:
        window.add_env_objects(item)

    window.set_agent(AgentRandom(3))
    # window.set_agent(AgentNN_Simple(4))

    window.make_invisible()
    # pyglet.app.run()
    clock_counter = 0
    max_ticks = 2000
    game_score = 0
    game_over = None
    while clock_counter < max_ticks:
        print ("clock: ", clock_counter)
        # window.on_draw()
        game_over, game_score = window.update(0)
        clock_counter += 1
    print ("Game Over: {}, Game Score: {}".format(game_over, game_score))

print ("GAME OVER")
