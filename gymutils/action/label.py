from gymutils.env.name import get_base_name


ACTION_LABELS = {
    'Pong': ['None', 'Fire', 'Up', 'Down', 'Fire Up', 'Fire Down'],
    'Breakout': ['None', 'Fire', 'Right', 'Left'],
}


def get_action_labels(env_name):
    return ACTION_LABELS[get_base_name(env_name)]
