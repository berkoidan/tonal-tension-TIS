import numpy as np

def main_analysis(c, t, mkey, mode):
    chords, leaves, seq = get_leaves_chords(t)
    
    global harm_f
    harm_f = 1
    
    global m_mode
    m_mode = mode
    
    ckey = midi2chroma(mkey)
    
    vkey = extract_harm_functions(ckey)
    
    tam_candidates = c.shape[0]
    n_candidates = np.zeros((c.shape[0], 6))
    n_candidates_lerdahl = np.zeros((c.shape[0], 6))
    vs = np.zeros((c.shape[0], 6))
    vl = np.zeros((c.shape[0], 6))
    
    n_candidates, vs = TIS_select_candidates(t, c, seq, vkey)
    n_candidates_lerdahl, vl = lerdahl_select_candidates(t, c, seq, mkey)
    
    return vs, vl

