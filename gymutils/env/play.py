import gym
from gym.utils.play import play


def play_with_cb(env_name, fps=60, zoom=3):
    def cb(*args):
        print('a:', args[2])
        print('r:', args[3]) if args[3] != 0 else None
    env = gym.make(env_name)
    play(env, fps=fps, zoom=zoom, callback=cb)


def play_all_atari_envs(n_episodes=10, v=4, deterministic=False, noframeskip=True, fps=60, zoom=3, callback=None):
    for game in ['alien', 'amidar', 'assault', 'asterix', 'asteroids', 'atlantis',
        'bank_heist', 'battle_zone', 'beam_rider', 'berzerk', 'bowling', 'boxing', 'breakout', 'carnival',
        'centipede', 'chopper_command', 'crazy_climber', 'demon_attack', 'double_dunk',
        'elevator_action', 'enduro', 'fishing_derby', 'freeway', 'frostbite', 'gopher', 'gravitar',
        'hero', 'ice_hockey', 'jamesbond', 'journey_escape', 'kangaroo', 'krull', 'kung_fu_master',
        'montezuma_revenge', 'ms_pacman', 'name_this_game', 'phoenix', 'pitfall', 'pong', 'pooyan',
        'private_eye', 'qbert', 'riverraid', 'road_runner', 'robotank', 'seaquest', 'skiing',
        'solaris', 'space_invaders', 'star_gunner', 'tennis', 'time_pilot', 'tutankham', 'up_n_down',
        'venture', 'video_pinball', 'wizard_of_wor', 'yars_revenge', 'zaxxon']:
        name = ''.join([g.capitalize() for g in game.split('_')])

        if deterministic:
            name += 'Deterministic'
        elif noframeskip:
            name += 'NoFrameskip'

        name += "-v{}".format(v)
        env = gym.make(name)

        for i in range(n_episodes):
            print(name, "episode {}/{}".format(i + 1, n_episodes))
            play(env, fps=fps, zoom=zoom, callback=callback)
