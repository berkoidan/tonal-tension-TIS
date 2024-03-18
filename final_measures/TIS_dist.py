
from chord_operations.compare_chords import compare_chords
from chord_operations.harmotion import harmotion
from chord_operations.key_dist import key_dist

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
    v2 = abs(compare_chords(t1, t2)) / max_d
    
    # c) Compare distance between the chord and the key
    tkey, mod_key = vkey[0].normal_fft()
    v3 = key_dist(t2, tkey)
    
    # d) Compare distance between the chord and the harmonic functions
    tokey, mod_t = vkey[1].normal_fft()
    dokey, mod_d = vkey[2].normal_fft()
    sdkey, mod_s = vkey[3].normal_fft()
    v4 = abs(harmotion(t2, tkey, tokey, dokey, sdkey, tf))
    
    vt = (v2 * 1.5 + 3.5 * v3 + 1.1 * v4)
    
    print("TIS_dist", c1, c2, vkey, tf, "\t", v2, v3, v4, vt)
    
    return v2, v3, v4, vt

