import numpy as np


def pad_to_fit_the_width(observation1, observation2):
    height1, width1, _ = observation1.shape
    height2, width2, _ = observation2.shape
    dtype = observation1.dtype
    if width1 > width2:
        new_observation2 = np.zeros([height2, width1, 3], dtype=dtype)
        offset = int((width1 - width2) / 2)
        new_observation2[:, offset:offset+width2, :] = observation2
        observation2 = new_observation2
    elif width2 > width1:
        new_observation1 = np.zeros([height1, width2, 3], dtype=dtype)
        offset = int((width2 - width1) / 2)
        new_observation1[:, offset:offset+width1, :] = observation1
        observation1 = new_observation1
    return observation1, observation2


def pad_to_fit_the_height(observation1, observation2):
    height1, width1, _ = observation1.shape
    height2, width2, _ = observation2.shape
    dtype = observation1.dtype
    if height1 > height2:
        new_observation2 = np.zeros([height1, width2, 3], dtype=dtype)
        offset = int((height1 - height2) / 2)
        new_observation2[offset:offset+height2, :, :] = observation2
        observation2 = new_observation2
    elif height2 > height1:
        new_observation1 = np.zeros([height2, width1, 3], dtype=dtype)
        offset = int((height2 - height1) / 2)
        new_observation1[offset:offset+height1, :, :] = observation1
        observation1 = new_observation1
    return observation1, observation2
