from pyglet.window import key
import numpy as np
from models import *
import torch
from torch.autograd import Variable
import torch.nn as nn

class AgentBase:
    def __init__(self, nb_actions):
        self.nb_actions = nb_actions

    def get_next_move(self, current_observation=None):
        raise(NotImplemented)

class AgentRandom(AgentBase):
    def __init__(self, nb_actions):
        super(AgentRandom, self).__init__(nb_actions)

    def get_next_move(self, current_observation=None):
        random_key = np.random.randint(0, self.nb_actions)

        return random_key

class AgentNN_Simple(AgentBase):
    def __init__(self, nb_actions):
        super(AgentNN_Simple, self).__init__(nb_actions)
        self.nn_model = LinearModel_BinaryMem(input_size=17, hidden_layer_sizes=(20,), ext_memory_size=4, output_size=nb_actions)

    def get_next_move(self, current_observation=None):
        chosen_action = None
        # Prepare model input
        current_observation_np = np.array(current_observation).reshape((1, -1))
        current_observation_var = Variable(torch.from_numpy(current_observation_np).float(), requires_grad=False)

        # Model output
        model_output = self.nn_model.forward(current_observation_var)
        chosen_action = np.argmax(model_output.data.cpu().numpy())
        return chosen_action
