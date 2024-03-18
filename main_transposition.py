from chord_operations.midi2chroma import *
from chord_operations.extract_harm_functions import *
from final_measures.TIS_select_candidates import select_candidates_TIS
from final_measures.lerdahl_select_candidates import *
from tree import HierarchicalTree

m1 = [[60, 64, 67, 72], [57, 65, 69, 72], [57, 65, 69, 74], [55, 65, 67, 71], [60, 64, 67, 72]]
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
def create_tree():
    t = HierarchicalTree('TR')
    n1 = t.addnode('TR')
    n2 = t.addnode('TR')
    n3 = n2.addnode('DR')
    n4 = n3.addnode('SR')
    n5 = n4.addnode('SR')
    n6 = n4.addnode('SR')
    seq = [n1.addnode('t'), n5.addnode('s'), n6.addnode('s'), n3.addnode('d'), n2.addnode('t')]
    return t, seq

t, seq = create_tree()
for i in range(len(seq)):
    seq[i].setChord(midi2chroma(m1[i]))

# Call the function
vkey = extract_harm_functions(ckey)
# m, a = lerdahl_select_candidates(None, m1, None, mkey)
m, a = select_candidates_TIS(t, m1, seq, vkey)
print(a)

print('-------')

# mkey = [60, 62, 64, 66, 67, 69, 71] # GMajor
mkey = [note + 7 for note in mkey]
m2 = [[note + 7 for note in row] for row in m1]
ckey = midi2chroma(mkey)
vkey = extract_harm_functions(ckey)
t, seq = create_tree()
for i in range(len(seq)):
    seq[i].setChord(midi2chroma(m2[i]))
    
m, a = select_candidates_TIS(t, m2, seq, vkey)

print(a)

