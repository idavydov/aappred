import os
import pickle


def load(fn):
    with open(fn, 'rb') as f:
        return pickle.load(f)


props = load('svm/props.pickle')
aap = load('svm/aap.pickle')


def predict(samples, model=props):
    return model.decision_function(samples)
