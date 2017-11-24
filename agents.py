from pyglet.window import key
import numpy as np

class AgentBase:
    def __init__(self, nb_actions):
        self.nb_actions = nb_actions

    def get_next_move(self, current_observation=None):
        raise(NotImplemented)

class AgentRandom(AgentBase):
    def __init__(self, nb_actions):
        super(AgentRandom, self).__init__(nb_actions)
        self.keys = dict(up=None, left=None, right=None, down=None)

    def get_next_move(self, current_observation=None):
        random_key = np.random.randint(0, 4)

        return random_key

class AgentNN_Simple(AgentBase):
    def __init__(self, nb_actions):
        super(AgentNN_Simple, self).__init__(nb_actions)
        self.keys = dict(up=None, left=None, right=None, down=None)

    def get_next_move(self, current_observation=None):
        return self.keys
