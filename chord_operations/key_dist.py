import numpy as np

def key_dist(chord, key):
    value = np.arccos(np.real(np.dot(chord, key)) / (np.linalg.norm(chord) * np.linalg.norm(key)))
    return value

