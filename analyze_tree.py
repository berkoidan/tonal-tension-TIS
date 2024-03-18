def analyze_tree(seq):
    stemp = seq
    k = [i for i, x in enumerate(seq) if x == 's']
    Tr = [None] * len(seq)
    for i in range(len(seq)):
        Tr[i] = seq[i]
    if k:
        for i in range(len(stemp)):
            if stemp[i+1] == 'd':
                t2 = tree('DR')
                t2 = t2.addnode(1, 'SR')
                t2 = t2.addnode(1, 'd')
                Tr[k[i]] = t2
                Tr[k[i+1]] = 0
                stemp[i] = 0
                stemp[i+1] = 0
            elif stemp[i+1] == 's':
                t2 = tree('SR')
                t2 = t2.addnode(1, 'SR')
                t2 = t2.addnode(1, 'SR')
                Tr[k[i]] = t2
                Tr[k[i+1]] = 0
                stemp[i+1] = 0
    t2.tostring()

