from chord_operations.midi2chroma import *
from chord_operations.extract_harm_functions import *
from final_measures.TIS_select_candidates import select_candidates_TIS
from final_measures.lerdahl_select_candidates import *
from tree import Tree

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
t = Tree('TR')
n1 = t.addnode('TR')
n2 = t.addnode('DR')
n3 = n1.addnode('t')
n4 = n2.addnode('SR')
n5 = n2.addnode('d')
n6 = n4.addnode('s')
seq = [n3, n6, n5]
# Call the function
c1 = midi2chroma(m1[0])
c2 = midi2chroma(m1[1])
vkey = extract_harm_functions(ckey)
# m, a = lerdahl_select_candidates(None, m1, None, mkey)
m, a = select_candidates_TIS(t, m1, seq, vkey)
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

