import matplotlib.pyplot as plt
import numpy as np

from Chord import NOTE_NAMES, Chord
from HirerarchicalTree.create_tree import find_harmonic_function
from final_measures.TIS_base import TIS

BASE_NOTE = 60
NOTE_COUNT = len(NOTE_NAMES)

def plot_heatmap(measures):
    fig, ax = plt.subplots()
    im = ax.imshow(measures, vmax=np.max(measures), cmap='viridis_r')

    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(NOTE_COUNT), labels=NOTE_NAMES)    
    ax.set_yticks(np.arange(6), labels=['M-M', 'M-m', 'M-o', 'm-M', 'm-m', 'm-o'])

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(measures.shape[0]):
        for j in range(measures.shape[1]):
            text = ax.text(j, i, round(measures[i, j], 2),
                       ha="center", va="center", color="w")

    ax.set_title("Angular Distance Between of Triads and Harmonic Function")
    fig.tight_layout()
    
    fig.savefig('Figures\\angular_func.png')
    for pos in [(0,0), (2, 1), (4, 1), (5, 0), (7, 0), (9, 1),(11, 2)]:
        circle = plt.Circle(pos, 0.5, fill=False, ec='red', lw=2.0)
        ax.add_patch(circle)
        
    for pos in [(0,4), (2, 5), (3, 3), (5, 4), (7, 4), (8, 3) ,(10, 3)]:
        circle = plt.Circle(pos, 0.5, fill=False, ec='purple', lw=2.0)
        ax.add_patch(circle)
    
    fig.savefig('Figures\\angular_func2.png')

    plt.close(fig)

measures = np.zeros((6, NOTE_COUNT))
for dist_type in range(6):
    for bass in range(BASE_NOTE, BASE_NOTE + NOTE_COUNT):
        if(dist_type == 0):
            vkey = Chord.majorHarmFunctions(BASE_NOTE)
            chord = Chord([bass, bass + 4, bass + 7])
        if(dist_type == 1):
            vkey = Chord.majorHarmFunctions(BASE_NOTE)
            chord = Chord([bass, bass + 3, bass + 7])
        if(dist_type == 2):
            vkey = Chord.majorHarmFunctions(BASE_NOTE)
            chord = Chord([bass, bass + 3, bass + 6])
        if(dist_type == 3):
            vkey = Chord.minorHarmFunctions(BASE_NOTE)
            chord = Chord([bass, bass + 4, bass + 7])
        if(dist_type == 4):
            vkey = Chord.minorHarmFunctions(BASE_NOTE)
            chord = Chord([bass, bass + 3, bass + 7])
        if(dist_type == 5):
            vkey = Chord.minorHarmFunctions(BASE_NOTE)
            chord = Chord([bass, bass + 3, bass + 6])
        tf = find_harmonic_function(chord, vkey).value        
        distance = abs(TIS.harmotion(chord, vkey, tf))
        print(vkey[0], chord, ':', tf, distance)
        measures[dist_type][bass - BASE_NOTE] = distance

plot_heatmap(measures)
