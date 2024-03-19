from final_measures.calculus_fundamental import *

def lerdahl_dist(m1, m2, skey):
    r1 = calculus_fundamental(m1)
    r2 = calculus_fundamental(m2)
    
    i = 0    
    circle_fifths = [5, 0, 7, 2, 9, 4, 11, 6, 1, 8, 3, 10]
    I1 = circle_fifths.index(r1)
    I2 = circle_fifths.index(r2)    
    j = abs(I1 - I2)
    
    ca1 = [r1]
    cb1 = [r1, (r1 + 7) % 12]
    x = 4
    if (r1 + 4) not in skey:
        x = 3
    cc1 = [r1, (r1 + 7) % 12, (r1 + x) % 12]
    
    if r2 not in m2:
        ca2 = []
    else:
        ca2 = [r2]
    
    if (r2 + 7) not in m2:
        cb2 = ca2
    else:
        cb2 = [r2, (r2 + 7) % 12]
    
    a = set(ca1).intersection(ca2)
    b = set(cb1).intersection(cb2)
    c = set(cc1).intersection(m2)
    d = set(skey).intersection(m2)
    
    k = 1 - len(a) + 2 - len(b) + 3 - len(c) + 7 - ((7 - len(m2)) + len(d))
    
    return i, j, k

