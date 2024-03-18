from chord_operations.midi2chroma import midi2chroma


def findsubmat(keys, subkeys):
    keys = ''.join(map(str, keys))
    subkeys = ''.join(map(str, subkeys))
    return keys.find(subkeys)

def extract_harm_functions(key):
    if key is None:
        mkey = [62, 64, 66, 67, 69, 71, 73]
        key = midi2chroma(mkey)

    tonic, dominant, subdominant = 0, 0, 0
    
    m_mode = 1
    if m_mode == 1:
        # Major tones:
        # 1) Duplicate octave of key vector:
        temp_key = key + key
        # 2) Find patron of major keys
        # print(''.join(map(str, temp_key)))
        index = findsubmat(temp_key, [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1])
        # index = index[0]
        if index >= 0:
            # 3) Extract function vectors
            major_chord_patron = [2, 0, 0, 0, 1, 0, 0, 1]
            tonic = [0] * 12
            dominant = [0] * 12
            subdominant = [0] * 12
            tindex = index
            sindex = index + 5
            dindex = index + 7
            for i in range(8):
                j = (tindex + i) % 12
                tonic[j] = major_chord_patron[i]
                j = (dindex + i) % 12
                dominant[j] = major_chord_patron[i]
                j = (sindex + i) % 12
                subdominant[j] = major_chord_patron[i]
    
    else:
        # Minor tones
        # 1) Duplicate octave of key vector:
        temp_key = key + key
        # 2) Find patron of minor keys
        index = findsubmat(temp_key, [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1])
        # 3) Extract function vectors
        if index >= 0:
            minor_chord_patron = [2, 0, 0, 1, 0, 0, 0, 1]
            major_chord_patron = [2, 0, 0, 0, 1, 0, 0, 1]
            tonic = [0] * 12
            dominant = [0] * 12
            subdominant = [0] * 12
            tindex = index[0]
            sindex = index[0] + 5
            dindex = index[0] + 7
            for i in range(8):
                j = (tindex + i) % 12
                tonic[j] = minor_chord_patron[i]
                j = (dindex + i) % 12
                dominant[j] = major_chord_patron[i]
                j = (sindex + i) % 12
                subdominant[j] = minor_chord_patron[i]
    
    vkey = [key, tonic, dominant, subdominant]
    return vkey

