from gymutils.env import get_env_infos


def get_action_labels(env_name):
    return get_env_infos(env_name)['action_labels']
