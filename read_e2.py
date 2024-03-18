import os
import numpy as np

filesList = [f for f in os.listdir('Audios') if f.startswith('prueba')]
N = len(filesList)
data = np.zeros((15, 144))
media = np.zeros((12, 12))

for i in range(N):
    print(filesList[i])
    with open(filesList[i], 'r') as fid:
        str = fid.readlines()
    
    str = [s.strip() for s in str]
    temp = []
    f = 0
    c = 1
    for j in range(len(str)):
        if str[j].startswith('A'):
            str2 = str[j].split(" ", 1)[1]
            c = 1
            f += 1
        else:
            str2 = str[j]
            c += 1
        temp = str2.split()
        v = [float(x) for x in temp]
        media[f, c] = np.mean([x for x in v if not np.isnan(x)])
    
    m = media.T.flatten()
    data[i, :] = m

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

