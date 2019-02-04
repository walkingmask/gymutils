import gym


SUFFIXES = [
    'Deterministic',
    'NoFrameskip',
    'Dense',
    'Sparse',
    'Full',
    'RotateXYZ',
    'RotateZ',
    'Rotate',
    'Parallel',
    'Hardcore',
    'ScreenBecomesBlack',
    '8x8',
    'Standup',
    'Generalized',
    'Continuous',
]


def get_base_name(env_name):
    if '-' in env_name:
        env_name = env_name.split('-')[0]
    for suffix in SUFFIXES:
        if suffix in env_name:
            env_name = env_name.replace(suffix, '')
    return env_name


def get_all_env_names():
    return [env_spec.id for env_spec in gym.envs.registry.all()]


def get_all_env_ids():
    return get_all_env_names()
