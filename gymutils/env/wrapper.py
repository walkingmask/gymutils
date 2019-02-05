import random

import gym
from gymutils.action import get_random_action


def get_random_steps(max_steps):
    return random.randint(1, max_steps - 1)


def step_obs(env, action):
    obs, _, _, _ = env.step(action)
    return obs


def step(env, action=None, steps=None, only_obs=False):
    steps = steps if steps else get_random_steps(env.spec.max_episode_steps)
    for _ in range(steps - 1):
        action = action if action else get_random_action(env.action_space.n)
        _ = env.step(action)
    action = action if action else get_random_action(env.action_space.n)
    if only_obs:
        obs = step_obs(env, action)
        return obs
    else:
        return env.step(action)


def random_action_step(env, only_obs=False):
    return step(env, None, 1, only_obs)


def random_step(env, action=None, only_obs=False):
    return step(env, action, None, only_obs)


def get_a_obs(env_name, action=None, steps=None, return_env=False):
    env = gym.make(env_name)
    _ = env.reset()
    obs = step(env, action, steps, True)
    if return_env:
        return obs, env
    else:
        return obs


class ObsEnv:
    def __init__(self, env_name, action=None, steps=None):
        self.env_name = env_name
        obs, env = get_a_obs(env_name, action, steps, True)
        self.obs = obs
        self.env = env

    def reset(self, action=None, steps=None):
        obs, env = get_a_obs(self.env_name, action, steps, True)
        self.obs = obs
        self.env = env
        return obs

    def step(self, action=None, steps=None):
        return step(self.env, action, steps, True)
