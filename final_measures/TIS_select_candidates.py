import numpy as np

from chord_operations.chord_qual import *
from final_measures.TIS_dist import *
from final_measures.TIS_global_surface import *
from final_measures.TIS_voices2 import *

def select_candidates_TIS(t, chords, seq, vkey):
    # Vamos a calcular la distancia que hay entre dos acordes bas�ndonos en la
    # harmonic attraction lerdahl y voice_leading lerdahl.
    # Arbol construido = t
    # acordes de la sucesi�n = chords
    # �ndice de los nodos hoja = seq
    # Devolvemos un vector con las cuatro medidas:
    # --> v1: voice leading (harmonic attraction)
    # --> v2: distance
    # --> v3: tonal surface
    # --> v4: dissonance
    v = np.zeros((len(chords), 6))
    # Normalization
    # max_d = 0.94
    # max_t = max_d * (len(seq))
    c1 = chords[0]
    t1, mod_t1 = c1.normal_fft()
    # char = t.get(seq[0])
    v[0, 0], v[0, 3], v[0, 4], v[0, 5] = TIS_dist(c1, c1, vkey, seq[0].value)  # Distance between two chords
    v[0, 2] = (1 - abs(chord_qual(t1)))  # Dissonance measure
    # Voice-leading to select the best inversion: The higher the better
    # (maximization function)    
    for i in range(1, len(chords)):
        c1 = chords[i - 1]
        c2 = chords[i]
        t2, mod_t2 = c2.normal_fft()
        inversion, v[i, 1] = TIS_voices2(c1, c2, vkey)
        chords[i] = inversion
        # char = t.get(seq[i])
        v[i, 0], v[i, 3], v[i, 4], v[i, 5] = TIS_dist(c1, c2, vkey, seq[i].value)
        v[i, 2] = (1 - abs(chord_qual(t2)))
    # To calculate tension surface:
    # print(t, chords, seq)
    w_temp = TIS_global_surface(t, seq, vkey)  # /max_t;
    v[:, 1] = w_temp[:, 0]
    return chords, v

