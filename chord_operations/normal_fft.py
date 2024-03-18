import numpy as np

def normal_fft(chroma):
    N = 12
    W = [2, 11, 17, 16, 19, 7]
    T = np.zeros(N//2)

    mod_c = sum(chroma)
    
    T = np.fft.fft(chroma)
    T = T[1:7]
    
    for k in range(6):
        T[k] = (W[k]/mod_c) * T[k]
    
    return T, mod_c

