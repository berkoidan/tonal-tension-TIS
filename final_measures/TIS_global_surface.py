from final_measures.TIS_dist import TIS_dist
from final_measures.recursive_tree import recursive_tree
import numpy as np


def TIS_global_surface(t, seq, vkey):
    recursive_tree(t, vkey)
    print(t)
    new_fit = np.zeros((len(seq), 4))    
    for i in range(len(seq)):
        node = seq[i].parent
        counter = 0
        while node:
            new_fit[i] += TIS_dist(seq[i].chord, node.chord, vkey, node.value[0].lower())
            counter += 1
            node = node.parent
        new_fit[i] /= counter
    return new_fit
