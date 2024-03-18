from chord_operations.calculus_fundamental import *
import numpy as np


def lerdahl_dissonance(m, skey):
    # Tdiss = inversion+diat+scale_degree, where:
    # inversion = 2 if chord inverted, 0 otherwise
    # diat = 3 if a note not belonging to triad-chord, 4 if a note not
    # belonging to triad nor the scale, 0 otherwise
    # scale_degree = 1 if 3rd or 5th is in the melodic voice, 0 otherwise
    # NOTE: Scale_degree is not applied in this equation
    inversion = 0
    diat = 0
    scale_degree = 0
    r2 = calculus_fundamental(m)
    m = list(map(lambda key: key % 12, m))    
    if m[0] != r2:
        inversion = 2
    # Calculate degree:
    if m[-1] != r2:
        scale_degree = 1
    # Know if minor of major mode
    x = 4
    print(skey, m, r2)
    # v, I = np.where(skey == (r2 + 4) % 12)
    if skey.index((r2 + 4) % 12):
        x = 3
    # Calculate diat
    m = np.unique(m)
    diatm = [r2, (r2 + x) % 12, (r2 + 7) % 12]
    diatv1 = np.intersect1d(diatm, m)
    if len(diatv1) < len(m):
        diat = 3
    diatv2 = np.intersect1d(skey, m)
    if len(diatv2) < len(m):
        diat = 4
    tdiss = inversion + diat + scale_degree
    return tdiss

