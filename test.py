from Chord import Chord
from final_measures.TIS_base import TIS


C = Chord([60, 62])
D = Chord([62])


for i in range(5):
    TIS.angular(C.transpose(2 * i), D.transpose(2 * i))