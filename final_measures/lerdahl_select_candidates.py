import numpy as np
from final_measures.lerdahl_dist import *
from final_measures.lerdahl_dissonance import *
from final_measures.lerdahl_global_surface import *
from final_measures.lerdahl_voices2 import *

def lerdahl_select_candidates(t, chords, seq, skey):
    # Vamos a calcular la distancia que hay entre dos acordes bas�ndonos en la
    # harmonic attraction lerdahl y voice_leading lerdahl.
    # Arbol construido = t
    # acordes de la sucesi�n = chords
    # �ndice de los nodos hoja = seq
    # Devolvemos un vector con las cuatro medidas:
    # --> v1: voice leading (harmonic attraction)
    # --> v2: distance to the key
    # --> v3: tonal surface
    # --> v4: dissonance
    # --> v5:
    # --> v6:
    v = np.zeros((len(chords), 6))
    key = skey[0]
    # Normalization
    # max_d = 13
    # max_vl = 15.73
    # max_c = 7
    # max_t = max_c + max_d + max_d * (len(seq) - 1)
    # Voice-leading to select the best inversion: The higher the better
    # (maximization function)
    v[0, 1], v[0, 4], v[0, 5] = lerdahl_dist(chords[0], chords[0], key)
    v[0, 3] = lerdahl_dissonance(chords[0], key)
    for i in range(1, len(chords)):
        inversion, v[i, 0] = lerdahl_voices2(chords[i - 1], chords[i], key)
        chords[i] = inversion
        # Harmonic attraction rule: h=c*voice_leading/d, where c=10
        # (maximization function)
        v[i, 1], v[i, 4], v[i, 5] = lerdahl_dist(chords[i - 1], chords[i], key)
        dist_final = (v[i, 1] + v[i, 4] + v[i, 5])
        if dist_final == 0:
            v[i, 0] = 0
        else:
            v[i, 0] = v[i, 0] / dist_final
        v[i, 3] = lerdahl_dissonance(chords[i], key)
    # v[:, 2] = lerdahl_global_surface(t, chords, seq, skey)
    return chords, v

