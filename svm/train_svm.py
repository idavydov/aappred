#!/usr/bin/env python
import sys
import numpy as np
from pickle import dump
from sklearn.svm import SVC


def read_data(fn):
    l = []
    y = []
    with open(fn) as f:
        for line in f:
            vec = [float(v) for v in line.split()]
            y.append(vec[0])
            l.append(vec[1:])
    return np.array(l), np.array(y)


if __name__ == '__main__':
    X_tr, Y_tr = read_data(sys.argv[1])
    model = SVC(C=4, kernel='rbf', gamma=8, probability=True, tol=1e-6, random_state=1)
    model.fit(X_tr, Y_tr)

    with open(sys.argv[2], 'w') as out:
        dump(model, out)
