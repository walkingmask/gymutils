import numpy as np

from gymutils.observation.pad import pad_to_fit_the_height, pad_to_fit_the_width


def concat_horizontally(observations, margin_width=0):
    result = observations[0]
    for observation in observations[1:]:
        result, observation = pad_to_fit_the_height(result, observation)
        height, _, _ = result.shape
        margin = np.zeros([height, margin_width, 3], dtype=result.dtype)
        result = np.concatenate([result, margin, observation], axis=1)
    return result


def concat_vertically(observations, margin_height=0):
    result = observations[0]
    for observation in observations[1:]:
        result, observation = pad_to_fit_the_width(result, observation)
        _, width, _ = result.shape
        margin = np.zeros([margin_height, width, 3], dtype=result.dtype)
        result = np.concatenate([result, margin, observation], axis=0)
    return result


def concat_table(observations_table, margin_width=0, margin_height=0):
    columns = []
    for observations_column in observations_table:
        columns.append(concat_horizontally(observations_column, margin_width))
    return concat_vertically(columns, margin_height)
