import os

import numpy as np
from skimage.transform import rescale

from gymutils.observation.concat import concat_vertically
from gymutils.text_array.loader import get_char_dict_3D

from gymutils.observation.view import look


def generate_string_array_3D(char_dict_3D, string):
    blank = char_dict_3D[0]
    result = blank.copy()
    for char in string:
        char_3D = char_dict_3D[ord(char)]
        result = np.concatenate([result, char_3D, blank], axis=1)
    return result


def generate_text_array_3D(char_dict_3D, text, canvas_size=None):
    string_arrays = [generate_string_array_3D(char_dict_3D, string) for string in text]
    text_array = string_arrays[0]
    for string_array in string_arrays[1:]:
        text_array = concat_vertically([text_array, string_array])

    if canvas_size:
        if text_array.shape[0] > canvas_size[0] or text_array.shape[1] > canvas_size[1]:
            print("canvas size is not enough.")
            return None
        else:
            offset_y = int((canvas_size[0] - text_array.shape[0]) / 2)
            offset_x = int((canvas_size[1] - text_array.shape[1]) / 2)
            canvas = np.zeros([*canvas_size, 3])
            canvas[
                offset_y:offset_y+text_array.shape[0],
                offset_x:offset_x+text_array.shape[1]
            ] = text_array
            text_array = canvas

    return np.uint8(text_array * 255)


class TextArrayGenerator3D:
    def __init__(self, canvas_size=None, font_size=1):
        self.reset(canvas_size, font_size)

    def reset(self, canvas_size=None, font_size=1):
        self.canvas_size = canvas_size
        self.char_dict_3D = get_char_dict_3D(font_size)

    def generate(self, text):
        return generate_text_array_3D(self.char_dict_3D, text, self.canvas_size)
