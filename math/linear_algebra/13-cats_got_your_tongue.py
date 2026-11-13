#!/usr/bin/env python3
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenate two matrices along a specified axis."""
    return np.concatenate((mat1, mat2), axis=axis)
