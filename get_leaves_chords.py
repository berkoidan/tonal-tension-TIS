def get_leaves_chords(t):
    chords = []
    leaves = []
    i_chords = []
    iterator = t.depthfirstiterator()
    for i in iterator:
        if t.isleaf(i):
            leaf = t.getparent(i)
            chord = t.get(i)
            leaves.append(leaf)
            chords.append(chord)
            i_chords.append(i)
    return chords, leaves, i_chords

