import numpy as np

def study_stability(t2, n_children, n, chords):
    col = len(n_children)
    s_chords = np.zeros((1, col))
    for i in range(col):
        s_chords[i] = 1
        a = int(t2.get(n_children[i]))
        chords[a, 4]
    v, I = np.min(s_chords)
    content_n = t2.get(n_children[I[0]])
    return content_n

