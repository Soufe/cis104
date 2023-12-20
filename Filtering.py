import numpy as np

def filtering(arr, low=-np.inf, high=np.inf):
    flattened_arr = arr.flatten()
    filtered_elements = flattened_arr[(flattened_arr >= low) & (flattened_arr <= high)]
    return filtered_elements