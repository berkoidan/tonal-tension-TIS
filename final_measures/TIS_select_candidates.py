from enum import Enum
import numpy as np

from final_measures.TIS_dist import *
from final_measures.TIS_global_surface import *
from final_measures.TIS_voices2 import *

class TISFeatures():
    DistBetweenChords = 0
    DistToKey = 1
    DistToHarmFunc = 2
    Dissonance = 3
    VoiceLeading = 4
    HierarchicalTension = 5
    NumberOfFeatures = 6

def select_candidates_TIS(t, chords, seq, vkey):
    # --> v1: voice leading (harmonic attraction)
    # --> v2: distance
    # --> v3: tonal surface
    # --> v4: dissonance
    v = np.zeros((len(chords), 6))
    # Normalization
    # max_d = 0.94
    # max_t = max_d * (len(seq))
    prev = chords[0]
    # Voice-leading to select the best inversion: The higher the better
    # (maximization function)    
    for i in range(len(chords)):
        chord = chords[i]        
        inversion, v[i, TISFeatures.VoiceLeading] = TIS_voices2(prev, chord, vkey)
        chords[i] = inversion
        v[i, TISFeatures.DistBetweenChords], v[i, TISFeatures.DistToKey], v[i, TISFeatures.DistToHarmFunc], _ = TIS_dist(prev, chord, vkey, seq[i].value)
        v[i, TISFeatures.Dissonance] = TIS.dissonance(chord)
        prev = chord
    # To calculate tension surface:
    # print(t, chords, seq)
    w_temp = TIS_global_surface(t, seq, vkey)  # /max_t;
    v[:, TISFeatures.HierarchicalTension] = w_temp[:, 0]
    return chords, v


