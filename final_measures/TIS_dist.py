
from Chord import Chord
from chord_operations.harmotion import harmotion

def TIS_dist(c1, c2, vkey, tf):    
    # Calculates the DFT of the chroma
    t1, mod_c1 = c1.normal_fft()
    t2, mod_c2 = c2.normal_fft()
    
    # Operations:
    # a) Measure quality of the chord
    # v1 = abs(chord_qual(t2))
    # v1 = 1 - v1
    
    max_d = 64.8757

    # b) Compare two consecutive chords for the progression
    v2 = abs(Chord.euclid(c1, c2)) / max_d
    
    # c) Compare distance between the chord and the key    
    v3 = Chord.angular(c2, vkey[0])
    
    # d) Compare distance between the chord and the harmonic functions
    v4 = abs(harmotion(c2, vkey, tf))
    
    vt = (v2 * 1.5 + 3.5 * v3 + 1.1 * v4)
    
    print("TIS_dist", c1, c2, tf, "\t", v2, v3, v4, vt)
    
    return v2, v3, v4, vt

