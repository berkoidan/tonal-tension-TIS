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
    ax.set_yticks(np.arange(NOTE_COUNT), labels=NOTE_NAMES)
    ax.xaxis.tick_top()

    # Rotate the tick labels and set their alignment.
    # plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(NOTE_COUNT):
        for j in range(NOTE_COUNT):
            text = ax.text(j, i, round(measures[i, j], 2),
                       ha="center", va="center", color="w")

    ax.set_title("Dissonance of Triads")
    fig.tight_layout()
    fig.savefig('Figures\\dissonance.png')
    plt.close(fig)

measures = np.zeros((NOTE_COUNT, NOTE_COUNT))
for note1 in range(NOTE_COUNT):
    for note2 in range(NOTE_COUNT):
        chord = Chord([BASE_NOTE, BASE_NOTE + note1, BASE_NOTE + note2])        
        measures[note1][note2] = TIS.dissonance(chord)


plot_heatmap(measures)
