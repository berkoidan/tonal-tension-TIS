
from final_measures.TIS_base import TIS

def TIS_dist(c1, c2, vkey, tf):    
    # Calculates the DFT of the chroma
    
    # Operations:
    # a) Measure quality of the chord
    # v1 = abs(chord_qual(t2))
    # v1 = 1 - v1
    
    max_d = 64.8757

    # b) Compare two consecutive chords for the progression
    v2 = abs(TIS.euclid(c1, c2)) / max_d
    
    # c) Compare distance between the chord and the key    
    v3 = TIS.angular(c2, vkey[0])
    
    # d) Compare distance between the chord and the harmonic functions
    v4 = abs(TIS.harmotion(c2, vkey, tf))
    
    vt = (v2 * 1.5 + 3.5 * v3 + 1.1 * v4)
    
    print("TIS_dist", c1, c2, tf, "\t", v2, v3, v4, vt)
    
    return v2, v3, v4, vt

