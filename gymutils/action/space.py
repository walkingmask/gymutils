from gym.envs.registration import make


def get_action_space(env_name):
    return make(env_name).action_space.n
