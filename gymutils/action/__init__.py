import random


def get_random_action(action_space_n):
    return random.randint(0, action_space_n - 1)
