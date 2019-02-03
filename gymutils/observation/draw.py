import numpy as np


OBJ_COLORS = {
    'Pong': [[236, 236, 236], [213, 130,  74], [ 92, 186,  92]],
}


class TrajectoryDrawer:
    def __init__(self, env_name='Pong', alpha=0.5):
        self.env_name = env_name
        self.alpha = alpha
        self.drawing = None

    def _get_shadows(self, observation):
        shadows = []
        for color in OBJ_COLORS[self.env_name]:
            shadow = np.zeros([210, 160, 3])
            shadow[34:194] = observation[34:194] == color
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
