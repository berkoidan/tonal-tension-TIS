import os, sys
import numpy as np
import matplotlib.pyplot as plt
from progressions import PROGRESSIONS

def read_samples_from_file(file):
    with open(file, 'r') as fid:
        lines = fid.readlines()
    datatext = ''.join(lines).split('AUDIO')
    datatext = [sample.replace('\n', ' ').replace('/', '').replace(';', '') for sample in datatext if sample.strip()]
    return datatext

def parse_sample(sample):
    prog_id, sample = sample.split('.wav')
    sample = np.array([float(x) for x in sample.strip().split()])
    prog_id = int(prog_id.strip('e'))
    return prog_id, sample

def read_samples(rootdir):
    filesList = [os.path.join(rootdir, file) for file in os.listdir(rootdir) if file.startswith('p')]
    samples = {}

    for i in range(len(filesList)):                
        samples_text = read_samples_from_file(filesList[i])
        for sample in samples_text:        
            prog_id, sample = parse_sample(sample)
            if prog_id not in samples:
                samples[prog_id] = []
            samples[prog_id].append(sample)
    
    return list(map(lambda prog_id: ProgressionSample(prog_id, pad_samples(samples[prog_id])), samples))    

def pad_samples(prog_samples):
    max_length = max(map(lambda sample: len(sample), prog_samples))    
    as_np = np.zeros((len(prog_samples), max_length))
    for j in range(len(prog_samples)):
        as_np[j][:] = np.pad(prog_samples[j], (max_length-len(prog_samples[j]),0), mode='constant', constant_values=50)
    return as_np
    
def plotgraph(graphtitle, data, err):
    t = np.arange(1, len(data[0])+1)

    fig, ax = plt.subplots()
    for i in range(len(data)):
        ax.plot(t, data[i])
        if err is not None:
            ax.errorbar(t, data[i], yerr=err, fmt='none')

    ax.set(xlabel='X', ylabel='Y', title=graphtitle)
    ax.grid()

    fig.savefig("test.png")
    plt.show()
    
class ProgressionSample():
    def __init__(self, progression_id, samples):
        self.progression_id = progression_id
        self.samples = samples
        self.chords_count = len(PROGRESSIONS[self.progression_id][1])
    
    def get_time_x(self):
        return np.arange(1, self.chords_count + 1, (self.chords_count) / len(self.samples[0]))
    
    def get_chords_x(self):
        return np.arange(1, self.chords_count + 1)
        
    def get_plain(self):
        return self.samples
    
    def get_normalized(self):
        result = np.zeros(self.samples.shape)
        for i in range(len(self.samples)):
            min_val = np.min(self.samples[i])
            max_val = np.max(self.samples[i])
            result[i] = (self.samples[i] - min_val) / (max_val - min_val)
        return result
    
    def get_mean(self):
        norm = self.get_normalized()
        return np.mean(norm, axis=0), np.std(norm, axis=0)
    
    def get_participants_model(self):
        return np.array(list(map(np.mean, np.array_split(self.get_mean()[0], self.chords_count))))

def figure_path(prog_id, id, name):
    dir_path = f'Figures\\Progression{prog_id}'    
    if not os.path.isdir(dir_path): 
        os.makedirs(dir_path)
    
    return os.path.join(dir_path, f'{id:02} {name}.png')
    

def plotgraph(prog_samples):
    FIGSIZE = (9, 4)
    
    # Plain samples
    fig, ax = plt.subplots(figsize=FIGSIZE)
    chords_x = prog_samples.get_chords_x()
    time_x = prog_samples.get_time_x()
    plt.xticks(chords_x)
    ax.set_ylim([0, 100])
    for sample in prog_samples.get_plain():
        ax.plot(time_x, sample)
    ax.set(xlabel='Event Number', ylabel='Instantaneous tonal tension', title=f'Progression {prog_samples.progression_id}: Plain Samples')
    ax.grid()
    fig.savefig(figure_path(prog_samples.progression_id, 0, 'plain'))
    plt.close(fig)
    
    # normalized samples
    fig, ax = plt.subplots(figsize=FIGSIZE)    
    for sample in prog_samples.get_normalized():
        ax.plot(time_x, sample)
    ax.set(xlabel='Event Number', ylabel='Instantaneous tonal tension', title=f'Progression {prog_samples.progression_id}: Normalized Samples')
    ax.grid()
    fig.savefig(figure_path(prog_samples.progression_id, 1, 'normalized'))
    plt.close(fig)
    
    mean, std = prog_samples.get_mean()
    # normalized samples
    fig, ax = plt.subplots(figsize=FIGSIZE)
    ax.set_ylim([0, 1])
    ax.errorbar(time_x, mean, yerr=std, fmt='c,')
    ax.plot(time_x, mean)
    ax.set(xlabel='Event Number', ylabel='Instantaneous tonal tension', title=f'Progression {prog_samples.progression_id}: Mean Samples')
    ax.grid()
    fig.savefig(figure_path(prog_samples.progression_id, 2, 'mean'))
    plt.close(fig)
    
    participants_model = prog_samples.get_participants_model()
    # normalized samples
    fig, ax = plt.subplots(figsize=FIGSIZE)    
    ax.set_ylim([0, 1])
    ax.plot(chords_x, participants_model)
    ax.plot(chords_x, participants_model, 'gD')
    ax.set(xlabel='Event Number', ylabel='Instantaneous tonal tension', title=f'Progression {prog_samples.progression_id}: Participants Tension')
    ax.grid()
    fig.savefig(figure_path(prog_samples.progression_id, 3, 'descrete'))
    plt.close(fig)

if __name__ == '__main__':    
    result_path = sys.argv[1]

    samples = read_samples(result_path)

    for prog in samples:
        plotgraph(prog)
