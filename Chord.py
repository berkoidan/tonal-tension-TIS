import numpy as np

NOTE_NAMES = ['c', 'c#', 'd', 'eb', 'e', 'f', 'f#', 'g', 'ab', 'a', 'bb', 'b']

class Chord():
    Major = True
    Minor = False
    
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
    
    def __contains__(self, element):
        if isinstance(element, Chord):
            if len(element) > 1:
                raise Exception("Chord should has exactly one note")
            element = element.notes[0]
        return any(map(lambda note: note % 12 == element % 12, self.notes))
    
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
    
    def tis(self):
        from final_measures.TIS_base import TISPoint
        return TISPoint(self)
