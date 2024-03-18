import numpy as np

from chord_operations.compare_chords import compare_chords
from chord_operations.harmotion import harmotion
from chord_operations.key_dist import key_dist
from chord_operations.midi2chroma import midi2chroma
from chord_operations.normal_fft import normal_fft

def TIS_dist(c1, c2, vkey, tf):    
    # Calculates the DFT of the chroma
    t1, mod_c1 = normal_fft(c1)
    t2, mod_c2 = normal_fft(c2)
    
    # Operations:
    # a) Measure quality of the chord
    # v1 = abs(chord_qual(t2))
    # v1 = 1 - v1
    
    max_d = 64.8757

    # b) Compare two consecutive chords for the progression
    v2 = abs(compare_chords(t1, t2)) / max_d
    
    # c) Compare distance between the chord and the key
    tkey, mod_key = normal_fft(vkey[0])
    v3 = key_dist(t2, tkey)
    
    # d) Compare distance between the chord and the harmonic functions
    tokey, mod_t = normal_fft(vkey[1])
    dokey, mod_d = normal_fft(vkey[2])
    sdkey, mod_s = normal_fft(vkey[3])
    v4 = abs(harmotion(t2, tkey, tokey, dokey, sdkey, tf))
    
    vt = (v2 * 1.5 + 3.5 * v3 + 1.1 * v4)
    
    print("TIS_dist", c1, c2, vkey, tf, "\t", v2, v3, v4, vt)
    
    return v2, v3, v4, vt

