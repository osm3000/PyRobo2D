from pyglet.window import key
import numpy as np
class AgentBase:
    pass

class AgentRandom(AgentBase):
    def __init__(self):
        super(AgentRandom, self).__init__()
        self.keys = dict(up=None, left=None, right=None, down=None)

    def get_next_move(self):
        random_key = np.random.randint(0, 3)
        for key in self.keys:
            self.keys[key] = False

        if random_key == 0:
            self.keys['up'] = True
        elif random_key == 1:
            self.keys['left'] = True
        elif random_key == 2:
            self.keys['right'] = True
        elif random_key == 3:
            self.keys['down'] = True

        return self.keys

class AgentKeyBoard(AgentBase):
    def __init__(self):
        super(AgentKeyBoard, self).__init__()
        self.keys = dict(up=None, left=None, right=None, down=None)

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

    def get_next_move(self):
        return self.keys
