import numpy as np
from PIL import Image


def _preprocess(observation):
    observation = observation.copy()
    if type(observation) != np.uint8:
        observation = np.uint8(observation)
    if observation.max() <= 1:
        observation *= 255
    return observation


def look(observation):
    Image.fromarray(_preprocess(observation)).show()


def save(observation, path, name, prefix='', suffix='', ext='png'):
    path = "{}/{}{}{}.{}".format(path, prefix, name, suffix, ext)
    Image.fromarray(_preprocess(observation)).save(path)
