import os

import numpy as np
from skimage.transform import rescale


def get_char_list_from_file():
    char_list_path = os.path.join(os.path.dirname(__file__), 'char_list.txt')
    with open(char_list_path, 'r') as f:
        lines = f.readlines()
    char_list = []
    for i in range(0, len(lines), 10):
        char_list.append([list(line.strip()) for line in lines[i:i+9]])
    return char_list


def get_char_dict():
    char_list = get_char_list_from_file()
    char_dict = {}
    for i in range(127):
        if i < 32:
            char_dict[i] = char_list[0]
        else:
            char_dict[i] = char_list[i - 31]
    return char_dict


def _3D(char):
    return np.stack([np.array(char, dtype=np.float) for _ in range(3)], axis=2)


def _rescale(char, zoom):
    return rescale(char, zoom, mode='constant', cval=0, multichannel=True, anti_aliasing=False)


def get_char_dict_3D(font_size=1):
    char_list = get_char_list_from_file()
    char_dict_3D = {}
    for i in range(127):
        if i < 32:
            char = _3D(char_list[0])
        else:
            char = _3D(char_list[i - 31])
        char_dict_3D[i] = _rescale(char, font_size)
    return char_dict_3D
