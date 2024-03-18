def lerdahl_global_surface(t, chords, seq, skey):
    # Vamos a calcular los predominant chords basados en el �rbol que ya
    # tenemos construido previamente:
    # Arbol construido = t
    # acordes de la sucesi�n = chords
    # �ndice de los nodos hoja = seq
    skey = list(map(lambda key: key % 12, skey % 12))
    index = 1
    n = 1
    t2 = tree(t)
    t2, index = recursive_tree(t, t2, n, index, chords)
    fil, col = seq.shape
    new_fit = np.zeros((fil, col))
    # t2 es el �rbol con los acordes sustituidos (�ndices)
    index = 1
    # Construyamos �rbol para generar medidas de distancia entre y->xdom
    t3 = tree(t2)
    iterator = t2.breadthfirstiterator
    for i in iterator:
        ind1 = int(t2.get(i))
        temp = t2.getparent(i)
        if temp == 0:
            ld = 0
        else:
            ind2 = int(t2.get(temp))
            ld1, ld2, ld3 = lerdahl_dist(chords[ind1, :], chords[ind2, :], skey)
            ld = ld1 + ld2 + ld3
        t3 = t3.set(i, ld)
    for i in seq:
        p_i = t2.getparent(i)
        while p_i != 0 and t2.get(p_i) == t2.get(i):
            p_i = t2.getparent(p_i)
        if p_i == 0:
            new_fit[index] = 0
        else:
            chord1 = chords[int(t2.get(p_i)), :]
            chord2 = chords[int(t2.get(i)), :]
            new_fit[index] = lerdahl_surface(t3, chord1, chord2, p_i, skey)
        index = index + 1
    best_p = new_fit
    return best_p

