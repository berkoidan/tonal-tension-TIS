import numpy as np

def harmotion(chord, key, tonic, dom, subd, harm_f):
    vtonic = np.subtract(key, tonic)
    vsub = np.subtract(key, subd)
    vdom = np.subtract(key, dom)
    vchord = np.subtract(key, chord)
    modc = np.linalg.norm(vchord)
    xc = vchord.real
    yc = vchord.imag

    value = None

    if harm_f == 't':  # Tonic function
        xt = vtonic.real
        yt = vtonic.imag
        modt = np.linalg.norm(vtonic)
        xpt = xc * xt
        ypt = yc * yt
        pt = 0        
        for i in range(len(xpt)):
            pt = pt + xpt[i] + ypt[i]
        temp = pt / (modt * modc)
        value = np.arccos(temp)
    elif harm_f == 's':  # Subdominant function
        xs = vsub.real
        ys = vsub.imag
        mods = np.linalg.norm(vsub)
        xps = xc * xs
        yps = yc * ys
        ps = 0
        for i in range(len(xps)):
            ps = ps + xps[i] + yps[i]
        temp = ps / (mods * modc)
        value = np.arccos(temp)
    elif harm_f == 'd':  # Dominant function
        xd = vdom.real
        yd = vdom.imag
        modd = np.linalg.norm(vdom)
        xpd = xc * xd
        ypd = yc * yd
        pd = 0        
        for i in range(len(xpd)):
            pd = pd + xpd[i] + ypd[i]
        temp = pd / (modd * modc)
        value = np.arccos(temp)

    return value

