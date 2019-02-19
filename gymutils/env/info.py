from gymutils.env.name import get_base_name


ENVS_INFOS = {
    'Pong': {
        'action_area': (slice(34, 194), slice(0, 160)),
        'action_space_n': 6,
        'action_labels': ['NOOP', 'FIRE', 'UP', 'DOWN', 'FIREUP', 'FIREDOWN'],
        'object_colors': [
            [236, 236, 236],  # ball
            [213, 130, 74],   # NPC
            [92, 186, 92],    # Player
        ],
        'backgrounds': [[144,  72,  17]],
    },
    'Breakout': {
        'action_area': (slice(32, 195), slice(8, 152)),
        'action_space_n': 4,
        'action_labels': ['NOOP', 'FIRE', 'RIGHT', 'LEFT'],
        'object_colors': [
            [200, 72, 72],
            [198, 108, 58],
            [180, 122, 48],
            [162, 162, 42],
            [72, 160, 72],
            [66, 72, 200],
        ],
        'backgrounds': [[0, 0, 0]],
    },
    'Alien': {
        'action_area': (slice(13, 173), slice(8, 160)),
        'action_space_n': 18,
        'action_labels': [
            'NOOP', 'FIRE', 'UP', 'RIGHT', 'LEFT', 'DOWN',
            'UPRIGHT', 'UPLEFT', 'DOWNRIGHT', 'DOWNLEFT',
            'UPFIRE', 'RIGHTFIRE', 'LEFTFIRE', 'DOWNFIRE',
            'UPRIGHTFIRE', 'UPLEFTFIRE', 'DOWNRIGHTFIRE', 'DOWNLEFTFIRE',
        ],
        'object_colors': [
            [132, 144, 252],
            [252, 144, 144],
            [252, 252,  84],
            [132, 252, 212],
        ],
        'backgrounds': [[0, 0, 0], [45, 50, 184], [80, 0, 132]],
    },
    'StarGunner': {
        'action_area': (slice(28, 188), slice(0, 160)),
        'action_space_n': 18,
        'action_labels': [
            'NOOP', 'FIRE', 'UP', 'RIGHT', 'LEFT', 'DOWN',
            'UPRIGHT', 'UPLEFT', 'DOWNRIGHT', 'DOWNLEFT',
            'UPFIRE', 'RIGHTFIRE', 'LEFTFIRE', 'DOWNFIRE',
            'UPRIGHTFIRE', 'UPLEFTFIRE', 'DOWNRIGHTFIRE', 'DOWNLEFTFIRE',
        ],
        'object_colors': [
            [214, 92, 92],
            [0, 28, 136],
            [45, 50, 184],
            [72, 160, 72],
            [128, 232, 128],
            [101, 160, 225],
            [142, 142, 142],
            [144, 252, 144],
        ],
        'backgrounds': [[0, 0, 0]],
    },
    'Boxing': {
        'action_area': (slice(36, 177), slice(32, 128)),
        'action_space_n': 18,
        'action_labels': [
            'NOOP', 'FIRE', 'UP', 'RIGHT', 'LEFT', 'DOWN',
            'UPRIGHT', 'UPLEFT', 'DOWNRIGHT', 'DOWNLEFT',
            'UPFIRE', 'RIGHTFIRE', 'LEFTFIRE', 'DOWNFIRE',
            'UPRIGHTFIRE', 'UPLEFTFIRE', 'DOWNRIGHTFIRE', 'DOWNLEFTFIRE',
        ],
        'object_colors': [
            [214, 214, 214],
            [0, 0, 0],
        ],
        'backgrounds': [[110, 156, 66]],
    },
    'SpaceInvaders': {
        'action_area': (slice(0, 210), slice(0, 160)),
        'action_space_n': 6,
        'action_labels': ['NOOP', 'LEFT', 'RIGHT', 'FIRE', 'LEFTFIRE', 'RIGHTFIRE'],
        'object_colors': [
            [50, 132, 50],    # player
            [181, 83, 40],    # ship
            [142, 142, 142],  # bullet
            [134, 134, 29],   # invaders
            [151,  25, 122],  # rare invader
        ],
        'backgrounds': [[0, 0, 0]],
    },
}


def get_env_infos(env_name):
    return ENVS_INFOS[get_base_name(env_name)]
