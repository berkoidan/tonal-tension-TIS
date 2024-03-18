import numpy as np

from Chord import Chord

def harmotion(chord, vkey, harm_f):
    if harm_f == 't':  # Tonic function
        return Chord.angular_rel(vkey[0], chord, vkey[1])
    elif harm_f == 's':  # Subdominant function
        return Chord.angular_rel(vkey[0], chord, vkey[3])
    elif harm_f == 'd':  # Dominant function
        return Chord.angular_rel(vkey[0], chord, vkey[2])
    

