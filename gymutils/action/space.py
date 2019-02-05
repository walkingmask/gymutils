from gymutils.env import get_env_infos


def get_action_space_n(env_name):
    return get_env_infos(env_name)['action_space_n']
