from gymutils.env.name import get_base_name


ENVS_INFOS = {
    'Pong': {
        'action_area': (slice(34, 194), slice(0, 160)),
        'action_space_n': 6,
        'action_labels': ['None', 'Fire', 'Up', 'Down', 'Fire Up', 'Fire Down'],
        'object_colors': [[236, 236, 236], [213, 130, 74], [92, 186, 92]],
        'background': [144,  72,  17],
    },
    'Breakout': {
        'action_area': (slice(32, 195), slice(8, 152)),
        'action_space_n': 4,
        'action_labels': ['None', 'Fire', 'Right', 'Left'],
        'object_colors': [
            [200, 72, 72], [198, 108, 58], [180, 122, 48],
            [162, 162, 42], [72, 160, 72], [66, 72, 200],
        ],
        'background': [0, 0, 0],
    },
}


def get_env_infos(env_name):
    return ENVS_INFOS[get_base_name(env_name)]
