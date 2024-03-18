from chord_operations.midi2chroma import *
from chord_operations.extract_harm_functions import *
from final_measures.TIS_select_candidates import select_candidates_TIS
from final_measures.lerdahl_select_candidates import *

m1 = [[60, 64, 67], [60, 65, 69], [59, 62, 67]]
seq = ['t', 's', 'd']
# Global Matrix
harm_f = 2
# Establish the key where we are working
mkey = [60, 62, 64, 65, 67, 69, 71] # CMajor
# mkey = [60, 62, 63, 65, 67, 68, 71] # cminor
# mkey = [60, 62, 64, 66, 67, 69, 71] # GMajor
# mkey = [60, 62, 63, 66, 67, 69, 70] # gminor
# A minor
m_mode = 1
# Major Mode:
# m_mode = 1
# minor Mode:
# m_mode = 0
ckey = midi2chroma(mkey)
# t = tree('TR')
# t, n1 = t.addnode(1, 'TR')
# t, n2 = t.addnode(1, 'DR')
# t, n3 = t.addnode(n1, 't')
# t, n4 = t.addnode(n2, 'SR')
# t, n5 = t.addnode(n2, 'd')
# t, n6 = t.addnode(n4, 's')
# seq = [n3, n6, n5]
# Call the function
c1 = midi2chroma(m1[0])
c2 = midi2chroma(m1[1])
vkey = extract_harm_functions(ckey)
# m, a = lerdahl_select_candidates(None, m1, None, mkey)
m, a = select_candidates_TIS(None, m1, seq, vkey)
a
# mkey = [60, 62, 64, 66, 67, 69, 71] # GMajor
mkey = [note + 7 for note in mkey]
c1 = midi2chroma([note + 7 for note in m1[0]])
c2 = midi2chroma([note + 7 for note in m1[1]])
m2 = [[note + 7 for note in row] for row in m1]
ckey = midi2chroma(mkey)
vkey = extract_harm_functions(ckey)
m, a = select_candidates_TIS(None, m2, seq, vkey)

print(a)

