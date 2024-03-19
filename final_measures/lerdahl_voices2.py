from Chord import Chord
from chord_operations.calculus_fundamental import calculus_fundamental

def lerdahl_voices_helper(note, bass, triad, key):    
    if note in bass:
        return 3
    if note in triad:
        return 2
    if note in key:
        return 1
    return 4

def lerdahl_voices2(m1, m2, skey):
    inversion = m2
    num_notes = len(m2)
    bass = skey[0]
    r1 = calculus_fundamental(bass)    
    triad = Chord.major(r1) if (r1 + 4) in skey else Chord.minor(r1)
    max_dist = 0
    dist_temp = 0
    for j in range(num_notes):
        semitones = abs(m1[j] - m2[j])
        if semitones != 0:
            a = [lerdahl_voices_helper(m1[j], bass, triad, skey), lerdahl_voices_helper(m2[j], bass, triad, skey)]
            dist_temp += (a[1] / a[0]) * 1 / (semitones) ** 2
    max_dist = dist_temp
    return inversion, max_dist

