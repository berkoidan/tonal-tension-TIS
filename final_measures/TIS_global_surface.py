def TIS_global_surface(t, chords, seq, skey):
    skey = skey % 12
    index = 1
    n = 1
    t2 = tree(t)
    t2, index = recursive_tree(t, t2, n, index, chords)
    new_fit = np.zeros((len(seq), 4))
    index = 1
    t3 = tree(t2)
    iterator = t2.breadthfirstiterator()
    for i in iterator:
        ind1 = int(t2.get(i))
        temp = t2.getparent(i)
        if temp == 0:
            dtis1 = 0
            dtis2 = 0
            dtis3 = 0
            dtis = 0
        else:
            ind2 = int(t2.get(temp))
            m1 = chords[ind1, :]
            m2 = chords[ind2, :]
            c1 = midi2chroma(m1)
            c2 = midi2chroma(m2)
            char = t.get(temp)
            if char.lower().startswith('t'):
                harm_f = 't'
            elif char.lower().startswith('s'):
                harm_f = 's'
            elif char.lower().startswith('d'):
                harm_f = 'd'
            dtis1, dtis2, dtis3, dtis = TIS_dist(c1, c2, skey, harm_f)
        t3 = t3.set(i, [dtis1, dtis2, dtis3, dtis])
    for i in seq:
        p_i = t2.getparent(i)
        while p_i != 0 and t2.get(p_i) == t2.get(i):
            p_i = t2.getparent(p_i)
        if p_i == 0:
            chord1 = chords[int(t2.get(i)), :]
            c1 = midi2chroma(chord1)
            tt, _ = normal_fft(c1)
            tf = t.get(i).lower()
            new_fit[index, :] = TIS_dist(c1, c1, skey, tf[0])
        else:
            chord1 = chords[int(t2.get(p_i)), :]
            chord2 = chords[int(t2.get(i)), :]
            char = chord2
            tf = t.get(p_i).lower()
            new_fit[index, :] = TIS_surface(t3, chord1, chord2, p_i, skey, tf[0])
        index += 1
    return new_fit

