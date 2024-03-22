from Chord import Chord

PROGRESSIONS = [
    # example
    (Chord.majorHarmFunctions(60), [
        Chord([60, 64, 67, 72]),
        Chord([57, 60, 64, 72]),
        Chord([59, 65, 67, 74]),
        Chord([60, 64, 67, 72]),
        # Chord([60, 64, 67, 72]), 
        # Chord([57, 65, 69, 72]), 
        # Chord([57, 65, 69, 74]), 
        # Chord([55, 65, 67, 71]), 
        # Chord([60, 64, 67, 72]),
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
    ]),
    # e3-chopin
    (Chord.minorHarmFunctions(57), [
        Chord([60, 64, 69, 81]), 
        Chord([64, 68, 71, 74]), 
        Chord([58, 62, 64, 68]), 
        Chord([58, 61, 64, 67]), 
        Chord([57, 61, 64, 67]), 
        Chord([57, 60, 63, 66]), 
    ]),
    # e4-schumann
    (Chord.majorHarmFunctions(60), [
        Chord([57, 60, 62, 66]), 
        Chord([55, 59, 62, 65]), 
        Chord([48, 55, 60, 64]), 
        Chord([49, 55, 58, 64]), 
        Chord([50, 57, 62, 65]), 
        Chord([47, 55, 62, 65]), 
    ]),
    # e5-brahms
    (Chord.majorHarmFunctions(60), [
        Chord([55, 59, 62, 65]),
        Chord([53, 60, 62, 66]),
        Chord([55, 59, 65, 67]),        
        Chord([55, 60, 62, 67]),        
        Chord([55, 59, 67, 69]),        
        Chord([55, 59, 65, 67]),        
        Chord([48, 55, 60, 64]), 
    ]),
    # e6-debussy
    (Chord.majorHarmFunctions(60), [
        Chord([60, 64, 67, 72]), 
        # Chord([59, 62, 65, 68]), 
        Chord([60, 62, 65, 69]), 
        Chord([60, 64, 67, 69]), 
        # Chord([62, 65, 67, 71]), 
        Chord([57, 60, 64, 69]), 
        Chord([60, 62, 65, 69]), 
        # Chord([59, 62, 65, 67]), 
        # Chord([57, 60, 62, 65]), 
        # Chord([56, 59, 62, 64]), 
        # Chord([55, 57, 60, 64]), 
    ]),
    # e1-invented
    (Chord.majorHarmFunctions(60), [
        Chord([60, 64, 67, 72]), 
        Chord([60, 66, 69, 72]), 
        Chord([57, 61, 64, 67]), 
        Chord([53, 57, 62, 65]), 
        Chord([55, 59, 62, 67]), 
        Chord([60, 64, 67, 72]),
    ]),
    # e2-invented
    (Chord.majorHarmFunctions(60), [
        Chord([60, 64, 67, 72]), 
        Chord([57, 60, 65, 69]), 
        Chord([55, 59, 62, 65]), 
        Chord([53, 55, 60, 64]), 
        Chord([59, 62, 65, 67]), 
        Chord([60, 64, 67, 72]), 
        Chord([55, 59, 62, 65]), 
        Chord([60, 64, 67, 72]), 
        Chord([55, 59, 62, 65]), 
        Chord([60, 64, 67, 72]), 
        
    ]),
    # e3-invented
    (Chord.minorHarmFunctions(57), [
        Chord([57, 60, 64, 69]), 
        Chord([52, 55, 60, 64]), 
        Chord([50, 53, 57, 62]), 
        Chord([50, 53, 58, 62]), 
        Chord([52, 56, 59, 64]), 
        Chord([50, 56, 59, 64]), 
    ]),
    # e4-invented
    (Chord.majorHarmFunctions(60), [
        Chord([57, 60, 62, 66]),
        Chord([55, 59, 62, 65]),
        Chord([48, 55, 60, 64]),
        Chord([53, 57, 60, 65]),
        Chord([53, 57, 62, 65]),
        Chord([55, 59, 62, 65]),
    ]),
    # e5-invented
    (Chord.majorHarmFunctions(60), [
        Chord([57, 60, 62, 66]),
        Chord([55, 60, 62, 67]),
        Chord([55, 59, 67, 69]),
        Chord([55, 59, 65, 67]),        
        Chord([48, 57, 60, 64]),
        Chord([48, 55, 60, 64]),
    ]),
    # e6-invented
    (Chord.majorHarmFunctions(60), [
        Chord([60, 64, 67, 72]),
        Chord([64, 67, 72, 76]),
        Chord([60, 64, 67, 72]),
        Chord([57, 60, 64, 69]), 
        Chord([60, 65, 69, 72]),
        Chord([60, 64, 67, 72]),
    ]),
]