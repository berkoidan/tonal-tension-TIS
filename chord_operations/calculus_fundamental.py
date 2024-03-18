

def calculus_fundamental(m1):
    # Establish weights for the sub-harmonics obtained
    w1 = 10  # 8th descendent
    w2 = 5  # 5th descendent
    w3 = 3  # 3M descendent
    w4 = 2  # 7m descendent
    w5 = 1  # 2M descendent
    W = [[w1, 0, w5, 0, w3, 0, 0, w2, 0, 0, w4, 0],
         [0, w1, 0, w5, 0, w3, 0, 0, w2, 0, 0, w4],
         [w4, 0, w1, 0, w5, 0, w3, 0, 0, w2, 0, 0],
         [0, w4, 0, w1, 0, w5, 0, w3, 0, 0, w2, 0],
         [0, 0, w4, 0, w1, 0, w5, 0, w3, 0, 0, w2],
         [w2, 0, 0, w4, 0, w1, 0, w5, 0, w3, 0, 0],
         [0, w2, 0, 0, w4, 0, w1, 0, w5, 0, w3, 0],
         [0, 0, w2, 0, 0, w4, 0, w1, 0, w5, 0, w3],
         [w3, 0, 0, w2, 0, 0, w4, 0, w1, 0, w5, 0],
         [0, w3, 0, 0, w2, 0, 0, w4, 0, w1, 0, w5],
         [w5, 0, w3, 0, 0, w2, 0, 0, w4, 0, w1, 0],
         [0, w5, 0, w3, 0, 0, w2, 0, 0, w4, 0, w1]]
    
    array_chord = midi2chroma(m1)
    
    # Multiply vectors
    array_value = [0] * 12
    for j in range(12):
        array_value[j] = sum([W[j][k] * array_chord[k] for k in range(12)])
    
    index = array_value.index(max(array_value))
  
    return index

