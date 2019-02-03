import numpy as np


class PongBallTrajectoryDrawer:
    def __init__(self, alpha=0.5):
        self.alpha = alpha
        self.drawing = None

    def _get_ball_shadow(self, observation):
        return observation == 236

    def _alpha_blend(self, observation):
        return self.alpha * self.drawing + (1 - self.alpha) * observation

    def draw(self, observation):
        if self.drawing is None:
            self.drawing = observation
        else:
            ball_shadow = self._get_ball_shadow(observation)
            pre_drawing = self._alpha_blend(observation)
            self.drawing = ball_shadow * observation + (ball_shadow != True) * pre_drawing
        return np.uint8(self.drawing)
