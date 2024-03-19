import numpy as np

from Chord import Chord
from final_measures.TIS_select_candidates import select_candidates_TIS
from final_measures.lerdahl_select_candidates import lerdahl_select_candidates

def main_analysis(chords, tree, keynote, major):
    seq = list(tree.leaves())    
    
    mkey = Chord.majorHarmFunctions(keynote) if major else Chord.minorHarmFunctions(keynote)
 
    n_candidates, vs = select_candidates_TIS(tree, chords, seq, mkey)
    n_candidates_lerdahl, vl = lerdahl_select_candidates(tree, chords, seq, mkey)
    
    return vs, vl

