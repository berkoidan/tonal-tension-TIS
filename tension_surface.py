from chord_operations.calculus_fundamental import calculus_fundamental


def tension_surface(t, m1, m2):
    v = abs(m1[3] - m2[3])
    r1 = calculus_fundamental(m1)
    r2 = calculus_fundamental(m2)
    skey = [0, 2, 4, 5, 7, 9, 11]
    i = 0
    circle_fifths = [5, 0, 7, 2, 9, 4, 11, 6, 1, 8, 3, 10]
    I1 = circle_fifths.index(r1)
    I2 = circle_fifths.index(r2)
    j = abs(r2 - r1)
    ca1 = [r1]
    cb1 = [r1, (r1 + 7) % 12]
    x = 4
    I = skey.index((r1 + 4) % 12)
    if I == -1:
        x = 3
    ca2 = [r2]
    cb2 = [r2, (r2 + 7) % 12]
    x = 4
    I = skey.index((r2 + 4) % 12)
    if I == -1:
        x = 3
    cc2 = [r2, (r2 + 7) % 12, (r2 + x) % 12]
    a = list(set(ca1) & set(ca2))
    b = list(set(cb1) & set(cb2))
    c = list(set(cc1) & set(cc2))
    d = 0
    k = len(a) + len(b) + len(c) + d
    lerdahl_d = i + j + k
    return lerdahl_d

