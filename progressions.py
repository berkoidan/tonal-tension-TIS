from Chord import Chord

PROGRESSIONS = [
    # example
    (Chord.majorHarmFunctions(60), [
        Chord([60, 64, 67, 72]), 
        Chord([57, 65, 69, 72]), 
        Chord([57, 65, 69, 74]), 
        Chord([55, 65, 67, 71]), 
        Chord([60, 64, 67, 72]),
    ]),
    # e1-bach
    (Chord.majorHarmFunctions(60), [
        Chord([60, 64, 67, 72]), 
        Chord([59, 62, 67, 74]),
        Chord([58, 60, 64, 67]),
        Chord([57, 60, 65, 69]),
        Chord([55, 59, 62, 67]),
        Chord([60, 64, 67, 72]),
    ]),
    # e2-mozart
    (Chord.majorHarmFunctions(60), [
        Chord([60, 64, 67, 72]), 
        Chord([53, 62, 65, 69]), 
        Chord([55, 59, 62, 65]), 
        Chord([53, 55, 60, 64]), 
        Chord([59, 62, 65, 67]), 
        Chord([60, 64, 67, 72]), 
        Chord([55, 59, 62, 65]), 
        Chord([60, 64, 67, 72]), 
        Chord([55, 59, 62, 65]), 
        Chord([55, 59, 62, 65]), 
    ])
]