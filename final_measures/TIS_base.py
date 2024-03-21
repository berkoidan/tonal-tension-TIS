import numpy as np

from Chord import Chord

class TISPoint():
    def __init__(self, chord:Chord):
        if isinstance(chord, Chord):
            self.complex, _ = self.normal_fft(chord.chroma())
        elif isinstance(chord, np.ndarray):
            self.complex = chord
        else:
            raise Exception("Unkown type in TISPoint ctor")
    
    def normal_fft(self, chroma):
        N = 12
        W = [2, 11, 17, 16, 19, 7]
        T = np.zeros(N//2)
        
        mod_c = max(sum(chroma), 1)
        T = np.fft.fft(chroma)[1:7]
        return (T * W) / mod_c, mod_c
    
    def __sub__(self, other):
        new_val = np.subtract(self.complex, other.complex)
        return TISPoint(new_val)
    
    def __abs__(self):
        return np.linalg.norm(self.complex)
    
    def __mul__(self, other):
        value = np.dot(self.complex, np.conjugate(other.complex))
        return value
    
    def __str__(self):
        return str(self.complex)
    
    def __matmul__(self, other):
        cos = np.real(self * other) / (abs(self) * abs(other))
        return np.arccos(np.clip(cos, -1, 1))

class TIS():
    def dissonance(chord):
        max_dissonance = abs(Chord([0]).tis())
        distance = abs(chord.tis())
        value = distance / max_dissonance
        return 1 - value
    
    def euclid(c1, c2):
        return abs(c1.tis() - c2.tis())
    
    def angular(c1, c2):
        value = c1.tis() @ c2.tis()
        return value
    
    def angular_rel(rel, c1, c2):
        rel_tis = rel.tis()
        value = (rel_tis - c1.tis()) @ (rel_tis - c2.tis())        
        return value
    
    def harmotion(chord, vkey, harm_f):
        if harm_f == 't':  # Tonic function
            return TIS.angular_rel(vkey[0], chord, vkey[1])
        elif harm_f == 's':  # Subdominant function
            return TIS.angular_rel(vkey[0], chord, vkey[3])
        elif harm_f == 'd':  # Dominant function
            return TIS.angular_rel(vkey[0], chord, vkey[2])
    

 
    
