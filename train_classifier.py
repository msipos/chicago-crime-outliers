''' Running instructions:

  python train_classifier.py PREPPED_DATA.csv  NUM_DATA_POINTS

'''

import cPickle as pickle
import lib
import numpy as np
import sys
import sklearn.ensemble


num_samples = int(sys.argv[2])

training_data = np.zeros((num_samples, 4))
result_data = np.zeros(num_samples)
histogram = lib.WindowedHistogram(num_samples)

i = 0
with open(sys.argv[1], 'rb') as file:
    for row in file:
        arr = row.split(' ')
        id = arr[0]
        tod = float(arr[1])
        longitude = float(arr[2])
        latitude = float(arr[3])
        loc = int(arr[4])
        typ = int(arr[5])

        training_data[i, :] = [tod, longitude, latitude, loc]
        result_data[i] = typ
        histogram.add(typ)

        i += 1
        if i >= num_samples:
            break

classifier = sklearn.ensemble.RandomForestClassifier(n_estimators=200, max_depth=10)
classifier.fit(training_data, result_data)

pickle.dump(classifier, open('classifier.pickle', 'wb'), pickle.HIGHEST_PROTOCOL)
pickle.dump(histogram, open('histogram.pickle', 'wb'), pickle.HIGHEST_PROTOCOL)
