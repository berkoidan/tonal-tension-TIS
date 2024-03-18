from chord_operations.midi2chroma import *
from chord_operations.normal_fft import *
from final_measures.TIS_dist import *
import numpy as np


def TIS_voices2(m1, m2, vkey):
    inversion = m2
    tkey, a = normal_fft(vkey[0])
    c1 = midi2chroma(m1)
    c2 = midi2chroma(m2)
    t1, mod_c1 = normal_fft(c1)
    t2, mod_c2 = normal_fft(c2)
    dist_temp = 0
    for i in range(len(m1)):
        cnote1 = midi2chroma([m1[i]])
        tnote1, a = normal_fft(cnote1)
        cnote2 = midi2chroma([m2[i]])
        tnote2, a = normal_fft(cnote2)
        nsemitones = abs(m1[i] - m2[i])
        v1, v2, v3, distnotes = TIS_dist(cnote1, cnote2, vkey, 't')
        dist_temp = dist_temp + 1 / np.exp(0.05 * nsemitones * distnotes)
    min_dist = dist_temp
    return inversion, min_dist

