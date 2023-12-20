import numpy as np

def get_mean(data):
    return np.mean(data, axis=0)

def get_median(data):
    return np.median(data, axis=0)

def get_std(data):
    return np.std(data, axis=0)

def get_iris_data():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    return np.genfromtxt(url, delimiter=',', usecols=(0, 1, 2, 3))