import numpy as np

NOTE_NAMES = ['c', 'c#', 'd', 'eb', 'e', 'f', 'f#', 'g', 'ab', 'a', 'bb', 'b']

class Chord():
    def __init__(self, notes):
        self.notes = sorted(list(set(notes)))        
        
    def __len__(self):
        return len(self.notes)
    
    def __getitem__(self, key):
        return Chord([self.notes[key]])
    
    def __sub__(self, other):
        return self.notes[0] - other.notes[0]
    
    def __str__(self):
        notes = ' '.join(map(lambda note: NOTE_NAMES[note % 12], self.notes))
        return f'[{notes}]'
    
    def major(bass):
        return Chord([bass, bass + 4, bass + 7, bass + 12])

    def minor(bass):
        return Chord([bass, bass + 3, bass + 7, bass + 12])
    
    def majorScale(bass):
        return Chord([bass, bass + 2, bass + 4, bass + 5, bass + 7, bass + 9, bass + 11])
    
    def minorScale(bass):
        return Chord([bass, bass + 2, bass + 3, bass + 5, bass + 7, bass + 8, bass + 10])
    
    def majorHarmFunctions(bass):
        return [Chord.majorScale(bass), Chord.major(bass), Chord.major(bass + 7), Chord.major(bass + 5)]

    def minorHarmFunctions(bass):
        return [Chord.minorScale(bass), Chord.minor(bass), Chord.major(bass + 7), Chord.minor(bass + 5)]
    
    def transpose(self, semitones):
        return Chord(map(lambda note: note + semitones, self.notes))

    def chroma(self):
        chroma_vector = [0] * 12
        for note in self.notes:
            chroma_vector[note % 12] += 1
        return chroma_vector
    
    def normal_fft(self):
        N = 12
        W = [2, 11, 17, 16, 19, 7]
        T = np.zeros(N//2)
        
        chroma_vector = self.chroma()
        mod_c = sum(chroma_vector)
        T = np.fft.fft(chroma_vector)[1:7]
        for k in range(6):
            # skip first value of T, representing freq 0
            T[k] = (W[k]/mod_c) * T[k]
        
        return T, mod_c
