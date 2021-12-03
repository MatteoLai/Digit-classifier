import numpy as np

import warnings
warnings.filterwarnings("ignore", message="Persisting input arguments took")


# --- DATASET ---
def load_unlabeled_dataset_from_txt(filePath, featureCount):
    data = np.loadtxt(filePath, usecols=range(0, featureCount))
    return data

def load_labeled_dataset_from_txt(filePath, featureCount):
    data = np.loadtxt(filePath, usecols=range(0, featureCount))
    labels = np.loadtxt(filePath, usecols=[featureCount])

    return data, labels

def separate_pattern_classes(data, labels, class_count):
    patternCount=data.shape[0]
    result = np.zeros(class_count, dtype = np.ndarray)
    for i in range(class_count):
        result[i] = np.array([data[j] for j in range(patternCount) if labels[j]==i])

    return result
