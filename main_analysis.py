
from HirerarchicalTree.create_tree import create_tree
from final_measures.TIS_select_candidates import select_candidates_TIS
from final_measures.lerdahl_select_candidates import lerdahl_select_candidates
from progressions import PROGRESSIONS

SANITY_TRASPOSITION = False
COMPUTE_LERDAHL = False

def main_analysis(chords, vkey):
    print(list(map(str, chords)))
    print(list(map(str, vkey)))    
    
    tree, seq = create_tree(chords, vkey)
    print(list(map(str, seq)))
    print(tree)
 
    n_candidates, vs = select_candidates_TIS(tree, chords, seq, vkey)
    print("TIS")
    print(vs)
    
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
    
    