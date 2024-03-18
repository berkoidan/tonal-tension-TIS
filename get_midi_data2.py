def get_midi_data2(midi_matrix):
    f, c = midi_matrix.shape
    chords = []
    input = np.zeros((2, 3))
    input[0, :] = [midi_matrix[0, 2], midi_matrix[1, 2], midi_matrix[2, 2]]
    input[1, :] = [midi_matrix[3, 2], midi_matrix[4, 2], midi_matrix[5, 2]]
    for i in range(0, f, 3):
        c_temp = [midi_matrix[i, 2], midi_matrix[i+1, 2], midi_matrix[i+2, 2]]
        chords.append(c_temp)
    return chords

