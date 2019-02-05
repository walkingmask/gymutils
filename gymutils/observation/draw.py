from collections import namedtuple

from gymutils.env import get_env_infos
import numpy as np


class TrajectoryDrawer:
    def __init__(self, env_name='Pong-v0', alpha=0.5):
        self.env_name = env_name
        env_infos = get_env_infos(env_name)
        self.action_area = env_infos['action_area']
        self.object_colors = env_infos['object_colors']
        self.alpha = alpha
        self.drawing = None

    def get_env_name(self):
        return self.env_name

    def _get_shadows(self, observation):
        shadows = []
        for color in self.object_colors:
            _shadow = np.prod(observation[self.action_area] == color, axis=2, keepdims=True)
            shadow = np.zeros([*observation.shape[:-1], 1])
            shadow[self.action_area] = _shadow
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
