import os
from matplotlib import pyplot as plt
from sklearn.linear_model import Ridge, LinearRegression
import numpy as np
import sys

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from HirerarchicalTree.create_tree import create_tree
from final_measures.TIS_select_candidates import TISFeatures, select_candidates_TIS
from progressions import PROGRESSIONS
from read_e2 import figure_path, read_samples

def get_model_samples(seed):
    # number_of_chords = sum(map(lambda prog: len(prog[1]), PROGRESSIONS))
    samples_x = []
    samples_y = []
    for listener_sample in read_samples(sys.argv[1]):
        participant_model = listener_sample.get_participants_model()
        vkey, chords = PROGRESSIONS[listener_sample.progression_id]
        tree, seq = create_tree(chords, vkey) 
        _, features = select_candidates_TIS(tree, chords, seq, vkey)
        for i in range(len(chords)):
            samples_x.append(features[i])
            samples_y.append(participant_model[i])
    X_train, X_test, y_train, y_test = train_test_split(samples_x, samples_y, random_state=seed)
    return X_train, X_test, y_train, y_test


def train(X_train, X_test, y_train, y_test):
    model = LinearRegression()    
    model.fit(X_train, y_train)
    return model, model.score(X_test, y_test)

seed = 42
X_train, X_test, y_train, y_test = get_model_samples(seed)

model, score = train(X_train, X_test, y_train, y_test)
for listener_sample in read_samples(sys.argv[1]):
    participant_model = listener_sample.get_participants_model()
    vkey, chords = PROGRESSIONS[listener_sample.progression_id]
    tree, seq = create_tree(chords, vkey) 
    _, features = select_candidates_TIS(tree, chords, seq, vkey)    
    prediction = model.predict(features)
    
    fig, ax = plt.subplots()
    x = range(1, len(chords) + 1)
    ax.plot(x, participant_model)
    ax.plot(x, prediction)
    ax.set(xlabel='Event Number', ylabel='Instantaneous tonal tension', title=f'Progression {listener_sample.progression_id}: Listener vs. Prediction')
    ax.grid()
    fig.savefig(figure_path(listener_sample.progression_id, 4, 'prediction'))    
    plt.close(fig)    


# # Max Mean Squared Error = 5319
# TRAIN_OCCURENCE = 1000
# def train_models(samples_x, samples_y, train, TRAIN_OCCURENCE):
#     coeffs = np.zeros((TRAIN_OCCURENCE, TISFeatures.NumberOfFeatures))
#     mses = np.zeros(TRAIN_OCCURENCE)

#     for seed in range(TRAIN_OCCURENCE):
#         model, mses[seed] = train(samples_x, samples_y, seed)
#         coeffs[seed] = model.coef_
#         # coeffs[seed], mses[seed] = train(samples_x, samples_y, seed)
#         print(seed, mses[seed])
#     return coeffs,mses

# coeffs, mses = train_models(samples_x, samples_y, train, TRAIN_OCCURENCE)

# print(f"Mean Coefficient: {np.average(coeffs, axis=0)}")
# print(f"STD Coefficient: {np.std(coeffs, axis=0)}")

# print(f"Mean Mean Squared Error: {np.mean(mses)}")
# print(f"STD Mean Squared Error: {np.std(mses)}")

# n_samples, n_features = 10, 5
# rng = np.random.RandomState(0)
# y = rng.randn(n_samples)
# X = rng.randn(n_samples, n_features)

# print(X, y)



# clf = Ridge(alpha=1.0)
# clf.fit(X, y)
# print(clf.coef_)
# print(clf.score(X, y))