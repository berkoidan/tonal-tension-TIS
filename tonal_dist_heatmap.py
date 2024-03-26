import matplotlib.pyplot as plt
import numpy as np

from Chord import NOTE_NAMES, Chord
from final_measures.TIS_base import TIS

BASE_NOTE = 60
NOTE_COUNT = len(NOTE_NAMES)

def plot_heatmap(measures):
    fig, ax = plt.subplots()
    im = ax.imshow(measures, vmax=np.max(measures), cmap='viridis_r')

    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(NOTE_COUNT), labels=NOTE_NAMES)    
    ax.set_yticks(np.arange(5), labels=['M-M', 'M-m', 'm-m', 'M-o', 'm-o'])

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(measures.shape[0]):
        for j in range(measures.shape[1]):
            text = ax.text(j, i, round(measures[i, j], 2),
                       ha="center", va="center", color="w")

    ax.set_title("Euclid Distance Between of Triads")
    fig.tight_layout()
    
    fig.savefig('Figures\\distance.png')
    for pos in [(0,0), (2, 1), (4, 1), (5, 0), (7, 0), (9, 1),(11, 3)]:
        circle = plt.Circle(pos, 0.5, fill=False, ec='red', lw=2.0)
        ax.add_patch(circle)
    
    fig.savefig('Figures\\distance2.png')

    plt.close(fig)

measures = np.zeros((5, NOTE_COUNT))
for dist_type in range(5):
    for bass in range(BASE_NOTE, BASE_NOTE + NOTE_COUNT):
        if(dist_type == 0):
            chord1 = Chord([BASE_NOTE, BASE_NOTE + 4, BASE_NOTE + 7])
            chord2 = Chord([bass, bass + 4, bass + 7])
        if(dist_type == 1):
            chord1 = Chord([BASE_NOTE, BASE_NOTE + 4, BASE_NOTE + 7])
            chord2 = Chord([bass, bass + 3, bass + 7])
        if(dist_type == 2):
            chord1 = Chord([BASE_NOTE, BASE_NOTE + 3, BASE_NOTE + 7])
            chord2 = Chord([bass, bass + 3, bass + 7])
        if(dist_type == 3):
            chord1 = Chord([BASE_NOTE, BASE_NOTE + 4, BASE_NOTE + 7])
            chord2 = Chord([bass, bass + 3, bass + 6])
        if(dist_type == 4):
            chord1 = Chord([BASE_NOTE, BASE_NOTE + 3, BASE_NOTE + 7])
            chord2 = Chord([bass, bass + 3, bass + 6])
        distance = TIS.euclid(chord1, chord2)
        print(chord1, chord2, ':', distance)
        measures[dist_type][bass - BASE_NOTE] = distance

plot_heatmap(measures)
