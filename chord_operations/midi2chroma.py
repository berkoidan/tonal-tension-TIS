def midi2chroma(vector):
    chroma_vector = [0] * 12
    col = len(vector)
    for i in range(col):
        index = vector[i] % 12
        chroma_vector[index] += 1
    return chroma_vector

