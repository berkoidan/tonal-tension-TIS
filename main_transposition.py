from Chord import Chord
from final_measures.TIS_select_candidates import select_candidates_TIS
# from final_measures.lerdahl_select_candidates import *
from HierarchicalTree import HierarchicalTree
from final_measures.lerdahl_select_candidates import lerdahl_select_candidates

m1 = [Chord([60, 64, 67, 72]), Chord([57, 65, 69, 72]), Chord([57, 65, 69, 74]), Chord([55, 65, 67, 71]), Chord([60, 64, 67, 72])]
# Global Matrix
harm_f = 2
# Establish the key where we are working
mkey = Chord.majorHarmFunctions(60) # C Major
# mkey = [60, 62, 63, 65, 67, 68, 71] # cminor
# mkey = [60, 62, 64, 66, 67, 69, 71] # GMajor
# mkey = [60, 62, 63, 66, 67, 69, 70] # gminor

# Major Mode:
# m_mode = 1
# minor Mode:
# m_mode = 0

def create_tree():
    t = HierarchicalTree('TR')
    n1 = t.addnode('TR')
    n2 = t.addnode('DR')
    n3 = n2.addnode('DR')
    n4 = n3.addnode('SR')
    n5 = n4.addnode('SR')
    n6 = n4.addnode('SR')
    seq = [n1.addnode('t'), n5.addnode('s'), n6.addnode('s'), n3.addnode('d'), n2.addnode('t')]
    return t, seq

t, seq = create_tree()
for i in range(len(seq)):
    seq[i].setChord(m1[i])

# Call the function
# m, a = lerdahl_select_candidates(t, m1, seq, mkey)
m, a = select_candidates_TIS(t, m1, seq, mkey)
print(a)

print('-------')

# mkey = [60, 62, 64, 66, 67, 69, 71] # GMajor
m2 = list(map(lambda chord: chord.transpose(7), m1))
# mkey = list(map(lambda chord: chord.transpose(7), mkey))
mkey = Chord.majorHarmFunctions(67) # G Major

t, seq = create_tree()
for i in range(len(seq)):
    seq[i].setChord(m2[i])
    
# m, a = lerdahl_select_candidates(t, m2, seq, mkey)
m, a = select_candidates_TIS(t, m2, seq, mkey)
print(a)

