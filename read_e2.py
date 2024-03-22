import os, sys
import numpy as np
import matplotlib.pyplot as plt

from progressions import PROGRESSIONS


def normalize(datasets):
    for i in range(len(datasets)):
        min_val = np.min(datasets[i])
        max_val = np.max(datasets[i])
        datasets[i] = (datasets[i] - min_val) / (max_val - min_val)
    return datasets
    
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
    
    for prog_id in list(samples.keys()):
        samples[prog_id] = pad_samples(samples[prog_id])
    
    return samples

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

def plotgraph(prog_id, prog_samples):
    chords_count = len(PROGRESSIONS[prog_id][1])
    chords_x = np.arange(1, chords_count + 1)
    time_x = np.arange(1, chords_count + 1, (chords_count) / len(prog_samples[0]))
    
    dir_path = f'Figures\\Progression{prog_id}'    
    if not os.path.isdir(dir_path): 
        os.makedirs(dir_path)    
    
    
    # Plain samples
    fig, ax = plt.subplots()
    ax.set_ylim([0, 100])
    for sample in prog_samples:
        ax.plot(time_x, sample)
    ax.set(xlabel='Event Number', ylabel='Instantaneous tonal tension', title=f'Progression {prog_id}: Plain Samples')
    ax.grid()
    fig.savefig(os.path.join(dir_path, '00 plain.png'))
    plt.close(fig)
    
    # plt.ylim([0, 1])
    prog_samples = normalize(prog_samples)
    
    # normalized samples
    fig, ax = plt.subplots()    
    for sample in prog_samples:
        ax.plot(time_x, sample)
    ax.set(xlabel='Event Number', ylabel='Instantaneous tonal tension', title=f'Progression {prog_id}: Normalized Samples')
    ax.grid()
    fig.savefig(os.path.join(dir_path, '01 normalized.png'))
    plt.close(fig)
    
    mean = np.mean(prog_samples, axis=0)
    std = np.std(prog_samples, axis=0)
    # normalized samples
    fig, ax = plt.subplots()
    ax.set_ylim([0, 1])
    ax.errorbar(time_x, mean, yerr=std, fmt='c,')
    ax.plot(time_x, mean)
    ax.set(xlabel='Event Number', ylabel='Instantaneous tonal tension', title=f'Progression {prog_id}: Mean Samples')
    ax.grid()
    fig.savefig(os.path.join(dir_path, '02 mean.png'))
    plt.close(fig)
    
    participants_model = np.array(list(map(np.mean, np.array_split(mean, chords_count))))
    # normalized samples
    fig, ax = plt.subplots()    
    ax.set_ylim([0, 1])
    ax.plot(chords_x, participants_model)
    ax.plot(chords_x, participants_model, 'gD')
    ax.set(xlabel='Event Number', ylabel='Instantaneous tonal tension', title=f'Progression {prog_id}: Participants Tension')
    ax.grid()
    fig.savefig(os.path.join(dir_path, '03 descrete.png'))
    plt.close(fig)

result_path = sys.argv[1]
# result_path = 'c:\\Temp\\tonal-tension-TIS-master\\Experiment1\\Results'

samples = read_samples(result_path)

for prog in samples:
    plotgraph(prog, samples[prog])
