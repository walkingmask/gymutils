import random

from gymutils.action.label import get_action_labels
from gymutils.action.space import get_action_space_n


def get_random_action(action_space_n):
    return random.randint(0, action_space_n - 1)


__all__ = ['get_action_labels', 'get_action_space_n', 'get_random_action']
