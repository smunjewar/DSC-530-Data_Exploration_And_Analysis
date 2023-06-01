import math
import numpy as np
from scipy import stats as scistats

from collections import Counter


def replace_nan_with_value(x, y, value):
    x = np.array([v if v == v and v is not None else value for v in x])  # NaN != NaN
    y = np.array([v if v == v and v is not None else value for v in y])
    return x, y


def conditional_entropy(
    x, y, nan_strategy="replace", nan_replace_value=0.0, log_base: float = math.e
):

    if nan_strategy == "replace":
        x, y = replace_nan_with_value(x, y, nan_replace_value)
    elif nan_strategy == "drop":
        x, y = remove_incomplete_samples(x, y)
    y_counter = Counter(y)
    xy_counter = Counter(list(zip(x, y)))
    total_occurrences = sum(y_counter.values())
    entropy = 0.0
    for xy in xy_counter.keys():
        p_xy = xy_counter[xy] / total_occurrences
        p_y = y_counter[xy[1]] / total_occurrences
        entropy += p_xy * math.log(p_y / p_xy, log_base)
    return entropy


def theils_u(x, y, nan_strategy="replace", nan_replace_value=0.0):
    if nan_strategy == "replace":
        x, y = replace_nan_with_value(x, y, nan_replace_value)
    elif nan_strategy == "drop":
        x, y = remove_incomplete_samples(x, y)
    s_xy = conditional_entropy(x, y)
    x_counter = Counter(x)
    total_occurrences = sum(x_counter.values())
    p_x = list(map(lambda n: n / total_occurrences, x_counter.values()))
    s_x = scistats.entropy(p_x)
    if s_x == 0:
        return 1
    else:
        return (s_x - s_xy) / s_x
