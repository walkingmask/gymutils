from collections import namedtuple

import numpy as np


ENVS = {
    'Pong': {
        'action_space': (slice(34, 194), slice(0, 160)),
        'object_colors': [[236, 236, 236], [213, 130, 74], [92, 186, 92]],
    },
}


class TrajectoryDrawer:
    def __init__(self, env_name='Pong', alpha=0.5):
        self.env_name = env_name
        self.action_space = ENVS[env_name]['action_space']
        self.object_colors = ENVS[env_name]['object_colors']
        self.alpha = alpha
        self.drawing = None

    def get_env_name(self):
        return self.env_name

    def _get_shadows(self, observation):
        shadows = []
        for color in self.object_colors:
            shadow = np.zeros([210, 160, 3])
            shadow[self.action_space] = observation[self.action_space] == color
            shadows.append(shadow)
        return shadows

    def _alpha_blend(self, observation):
        return self.alpha * self.drawing + (1 - self.alpha) * observation

    def draw(self, observation):
        if self.drawing is None:
            self.drawing = observation
        else:
            self.drawing = self._alpha_blend(observation)
            for shadow in self._get_shadows(observation):
                self.drawing = shadow * observation + (shadow != True) * self.drawing
        return np.uint8(self.drawing)
