def lerdahl_voices2(m1, m2, skey):
    inversion = m2
    num_notes = len(m2)
    r1 = skey[0]
    ca = [r1]
    x = 4
    print(m1, m2, skey)
    print(list(enumerate(skey)))
    v = [i for i, x in enumerate(skey) if x == (r1 + 4) % 12]
    if not v:
        x = 3
    cc = [r1, (r1 + 7) % 12, (r1 + x) % 12]
    max_dist = 0
    m11 = [x % 12 for x in m1]
    
    m21 = [x % 12 for x in m2]
    dist_temp = 0
    for j in range(num_notes):
        semitones = abs(m1[j] - m2[j])
        if semitones != 0:
            a = [0, 0]
            a[0] = 4
            v = [i for i, x in enumerate(ca) if x == m11[j]]
            if not v:
                a[0] = 3
                v = [i for i, x in enumerate(cc) if x == m11[j]]
                if not v:
                    a[0] = 2
                    v = [i for i, x in enumerate(skey) if x == m11[j]]
                    if not v:
                        a[0] = 1
            a[1] = 4
            v = [i for i, x in enumerate(ca) if x == m21[j]]
            if not v:
                a[1] = 3
                v = [i for i, x in enumerate(cc) if x == m21[j]]
                if not v:
                    a[1] = 2
                    v = [i for i, x in enumerate(skey) if x == m21[j]]
                    if not v:
                        a[1] = 1
            dist_temp += (a[1] / a[0]) * 1 / (semitones) ** 2
    max_dist = dist_temp
    return inversion, max_dist

