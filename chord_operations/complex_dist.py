import numpy as np

def complex_dist(n1, n2):
    r_n1 = np.real(n1)
    i_n1 = np.imag(n1)
    r_n2 = np.real(n2)
    i_n2 = np.imag(n2)
    # J, K = np.shape(n1)
    K = len(n1)
    distance = 0
    for k in range(K):
        distance += ((r_n2[k] - r_n1[k]) ** 2 + (i_n2[k] - i_n1[k]) ** 2)
    distance = np.sqrt(distance)
    return distance

