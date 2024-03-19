
import numpy as np
from HirerarchicalTree.create_tree import create_tree
from final_measures.TIS_select_candidates import select_candidates_TIS
from final_measures.lerdahl_select_candidates import lerdahl_select_candidates
from progressions import PROGRESSIONS

SANITY_TRASPOSITION = False
COMPUTE_LERDAHL = False

TIS_weights = np.array([0, 0.158, 0, 0.303, 0.271, 0.318])

def main_analysis(chords, vkey):    
    
    tree, seq = create_tree(chords, vkey)
    print(' | '.join(map(str, seq)))
    print(tree)
 
    n_candidates, vs = select_candidates_TIS(tree, chords, seq, vkey)
    print("TIS")
    print(vs)
    tis_total = vs @ TIS_weights
    for i, chord in enumerate(chords):
        print(chord, '\t::', tis_total[i])
    
    if COMPUTE_LERDAHL:    
        n_candidates_lerdahl, vl = lerdahl_select_candidates(tree, chords, seq, vkey)
        print("Lerdahl")
        print(vl)
    
for i, progression in enumerate(PROGRESSIONS):
    key, chords = progression
    print()
    print(f"=========== Prog {i} ============")
    main_analysis(chords, key)
    
    if SANITY_TRASPOSITION:
        print()
        print(f"Sanity Transposition:")
        chords = list(map(lambda chord: chord.transpose(7), chords))
        key = list(map(lambda chord: chord.transpose(7), key))
        main_analysis(chords, key)
    
    