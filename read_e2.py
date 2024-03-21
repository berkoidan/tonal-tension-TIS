import os, sys
import numpy as np
import matplotlib.pyplot as plt

from progressions import PROGRESSIONS

def plotgraph(graphtitle, data):    
    t = np.arange(len(data[0]))

    fig, ax = plt.subplots()
    for i in range(len(data)):        
        ax.plot(t, data[i])

    ax.set(xlabel='X', ylabel='Y', title=graphtitle)
    ax.grid()

    fig.savefig("test.png")
    plt.show()
    

def normalize(datasets):
    for i in range(len(datasets)):
        min_val = np.min(datasets[i])
        max_val = np.max(datasets[i])
        datasets[i] = (datasets[i] - min_val) / (max_val - min_val)
    return datasets

def avg(datasets):    
    return np.array([np.average(datasets, axis=0),])
    
def get_samples(file):
    with open(file, 'r') as fid:
        lines = fid.readlines()
    datatext = ''.join(lines).split('AUDIO')
    datatext = [sample.replace('\n', ' ').replace('/', '').replace(';', '') for sample in datatext if sample.strip()]
    return datatext

def parse_sample(sample):
    progression, sample = sample.split('.wav')
    sample = np.array([float(x) for x in sample.strip().split()])
    progression = int(progression.strip('e'))
    # print("TEST", sample)
    return sample, progression

# result_path = sys.argv[1]
result_path = 'c:\\Temp\\tonal-tension-TIS-master\\Experiment1\\Results'

filesList = [os.path.join(result_path, f) for f in os.listdir(result_path) if f.startswith('p')]
N = len(filesList)
data = np.zeros((15, 144))
media = np.zeros((12, 12))

samples = {}


for i in range(N):
    print(filesList[i])
    listener = int(os.path.basename(filesList[i]).strip('p').strip('.txt'))
    datatext = get_samples(filesList[i])
    for sample in datatext:        
        sample, progression = parse_sample(sample)
        if progression not in samples:
            samples[progression] = []
        samples[progression].append(sample)
        # print(len(sample))
        
        # x = np.array_split(sample, len(PROGRESSIONS[progression][1]))
        # print("Progression", progression)
        # print(x)
print("TEST2")
# print(samples)
for progression in list(samples.keys()):
    prog_samples = samples[progression]
    # print("DEBUG i", i, prog)
    # max_length = max(map(lambda sample: len(sample), prog_samples))
    min_length = min(map(lambda sample: len(sample), prog_samples))
    as_np = np.zeros((len(prog_samples), min_length))
    print("TEST", list(map(lambda s: len(s), prog_samples)))
    for j in range(len(prog_samples)):
        as_np[j][:] = prog_samples[j][(len(prog_samples[j])-min_length):]
    samples[progression] = as_np
    
# print(samples)
for progression in samples:
    plotgraph(f'Progression {progression}', samples[progression])
    plotgraph(f'Progression {progression} Normalized', normalize(samples[progression]))
    plotgraph(f'Progression {progression} Averaged', avg(samples[progression]))
    print(samples[progression])
    
    # str = [s.strip() for s in str]
    # temp = []
    # f = -1
    # c = 0
    # for j in range(len(str)):
    #     if str[j].startswith('A'):
    #         str2 = str[j].split(" ", 1)[1]
    #         c = 0
    #         f += 1
    #     else:
    #         str2 = str[j]
    #         c += 1
    #     temp = str2.strip(';').split()        
    #     v = [float(x) for x in temp if x]
    #     print(len(v), v)
    #     if len(v) == 0:
    #         continue
    #     media[f, c] = np.mean([x for x in v if not np.isnan(x)])
    # print(media)
    
    # m = media.T.flatten()
    # print(m)
    # data[i, :] = m

 
# Get repeated values
# temp_uniq = [float(temp[0])]
# for k in range(1, len(temp)):
#     v = float(temp[k])
#     repeated = float(temp[k-1])
#     if repeated == v and temp_uniq[-1] != v:
#         temp_uniq.append(v)
#     if v == -1:
#         temp_uniq.append(v)
# 
# data[i] = temp_uniq

# data = data.T
# T = pd.DataFrame(data)
# T.to_csv('myDataFile.csv', index=False)
