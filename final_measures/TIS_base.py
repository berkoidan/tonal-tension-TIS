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
        print(chord, self.complex)
    
    def normal_fft(self, chroma):
        N = 12
        W = [2, 11, 17, 16, 19, 7]
        T = np.zeros(N//2)
        
        mod_c = max(sum(chroma), 1)
        T = np.fft.fft(chroma)[1:7]
        for k in range(6):            
            T[k] = (W[k] / mod_c) * T[k]
            
        return T, mod_c
    
    def __sub__(self, other):
        new_val = np.subtract(self.complex, other.complex)
        return TISPoint(new_val)
    
    def __abs__(self):
        return np.linalg.norm(self.complex)
    
    def __mul__(self, other):
        return np.dot(self.complex, other.complex)
    
    def __str__(self):
        return str(self.complex)
    
    def __matmul__(self, other):
        return np.arccos(np.real(self * other) / (abs(self) * abs(other)))

class TIS():
    def dissonance(chord):
        max_dissonance = abs(Chord([0]).tis())
        distance = abs(chord.tis())
        value = distance / max_dissonance
        return 1 - value
    
    def euclid(c1, c2):
        return abs(c1 - c2)
    
    def angular(c1, c2):        
        return c1.tis() @ c2.tis()
    
    def angular_rel(rel, c1, c2):
        rel_tis = rel.tis()
        return (rel_tis - c1.tis()) @ (rel_tis - c2.tis())
    
    def harmotion(chord, vkey, harm_f):
        if harm_f == 't':  # Tonic function
            return TIS.angular_rel(vkey[0], chord, vkey[1])
        elif harm_f == 's':  # Subdominant function
            return TIS.angular_rel(vkey[0], chord, vkey[3])
        elif harm_f == 'd':  # Dominant function
            return TIS.angular_rel(vkey[0], chord, vkey[2])
    

 
    
