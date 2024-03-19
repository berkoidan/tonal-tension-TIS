import numpy as np

from Chord import Chord
from HirerarchicalTree.create_tree import create_tree
from final_measures.TIS_select_candidates import select_candidates_TIS
from final_measures.lerdahl_select_candidates import lerdahl_select_candidates

def main_analysis(chords, keynote, major):    
    mkey = Chord.majorHarmFunctions(keynote) if major else Chord.minorHarmFunctions(keynote)
    tree, seq = create_tree(chords, mkey)
 
    n_candidates, vs = select_candidates_TIS(tree, chords, seq, mkey)
    n_candidates_lerdahl, vl = lerdahl_select_candidates(tree, chords, seq, mkey)
    
    return vs, vl

