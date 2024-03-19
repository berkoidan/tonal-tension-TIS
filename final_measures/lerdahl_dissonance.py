from Chord import Chord
from final_measures.calculus_fundamental import *


def lerdahl_dissonance_inversion(m, r2):
    return 2 if r2 not in m[0] else 0

def lerdahl_dissonance_scale_degree(m, r2, major):
    if (r2 + 7) in m[-1]:
        return 1
    
    if major and (r2 + 4) in m[-1]:
        return 1

    if not major and (r2 + 3) in m[-1]:
        return 1
    
    return 0

def lerdahl_dissonance_diat(m, r2, major, skey):
    triad = Chord.major(r2) if major else Chord.minor(r2)
    
    for i in range(len(m)):
        if m[i] not in triad:
            return 3
    
    for i in range(len(m)):
        if m[i] not in skey:
            return 4
    
    return 0


def lerdahl_dissonance(m, skey):
    # Tdiss = inversion+diat+scale_degree, where:
    # inversion = 2 if chord inverted, 0 otherwise
    # scale_degree = 1 if 3rd or 5th is in the melodic voice, 0 otherwise
    # diat = 3 if a note not belonging to triad-chord, 4 if a note not
    # belonging to triad nor the scale, 0 otherwise
   
    r2 = calculus_fundamental(m)
    major = (r2 + 4) in skey
    
    inversion = lerdahl_dissonance_inversion(m, r2)
    scale_degree = lerdahl_dissonance_scale_degree(m, r2, major)
    diat = lerdahl_dissonance_diat(m, r2, major, skey)

    tdiss = inversion + diat + scale_degree
    return tdiss

