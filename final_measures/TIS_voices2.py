from final_measures.TIS_dist import *
import numpy as np


def TIS_voices2(m1, m2, vkey):
    inversion = m2
    dist_temp = 0
    for i in range(len(m1)):
        cnote1 = m1[i]
        cnote2 = m2[i]
        nsemitones = abs(m1[i] - m2[i])
        v1, v2, v3, distnotes = TIS_dist(cnote1, cnote2, vkey, 't')
        dist_temp = dist_temp + 1 / np.exp(0.05 * nsemitones * distnotes)
    min_dist = dist_temp
    return inversion, min_dist

