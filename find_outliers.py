''' Running instructions:

  python find_outliers.py CHICAGO_CRIME_DATA.csv NUM_DATA_POINTS_AFTER  STOP_AFTER

'''

import cPickle as pickle
import lib
import numpy as np
import sys
import sklearn.ensemble


num_after = int(sys.argv[2])
stop_after = int(sys.argv[3])

classifier = pickle.load(open('classifier.pickle'))
histogram = pickle.load(open('histogram.pickle'))


i = 0
with open(sys.argv[1], 'rb') as file:
    for row in file:
        i += 1
        if i < num_after: continue
        if i > num_after+stop_after: break

        arr = row.split(' ')
        id = arr[0]
        tod = float(arr[1])
        longitude = float(arr[2])
        latitude = float(arr[3])
        loc = int(arr[4])
        typ = int(arr[5])


        query_data = np.matrix([tod, longitude, latitude, loc])

        PCs = classifier.predict_proba(query_data)
        PC = PCs[0, typ]
        pC = histogram.get_prop(typ)
        score = (PC - pC)/ pC

        print id, typ, score
