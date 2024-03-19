import numpy as np
from final_measures.lerdahl_dist import lerdahl_dist
from final_measures.lerdahl_surface import lerdahl_surface


def lerdahl_global_surface(t, chords, seq, vkey):
    # Vamos a calcular los predominant chords basados en el �rbol que ya
    # tenemos construido previamente:
    # Arbol construido = t
    # acordes de la sucesi�n = chords
    # �ndice de los nodos hoja = seq
    new_fit = np.zeros((len(seq), 3))
    # t2 es el �rbol con los acordes sustituidos (�ndices)
    # Construyamos �rbol para generar medidas de distancia entre y->xdom
    for i in range(len(seq)):    
        ind1 = int(t2.get(i))
        temp = t2.getparent(i)
        if temp == 0:
            ld = 0
        else:
            ind2 = int(t2.get(temp))
            ld1, ld2, ld3 = lerdahl_dist(chords[ind1, :], chords[ind2, :], vkey)
            ld = ld1 + ld2 + ld3
        t3 = t3.set(i, ld)
    for i in seq:
        p_i = t2.getparent(i)
        while p_i != 0 and t2.get(p_i) == t2.get(i):
            p_i = t2.getparent(p_i)
        if p_i == 0:
            new_fit[index] = 0
        else:
            chord1 = chords[int(t2.get(p_i)), :]
            chord2 = chords[int(t2.get(i)), :]
            new_fit[index] = lerdahl_surface(t3, chord1, chord2, p_i, vkey)
        index = index + 1
    best_p = new_fit
    return best_p

