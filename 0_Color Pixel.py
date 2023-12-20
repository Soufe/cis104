import numpy as np
import matplotlib.pyplot as plt

def pixel2img(fn):
  with open(fn, 'r') as f:
    h = int(f.readline().strip())
    w = int(f.readline().strip())
  pixel_data = np.genfromtxt(f, delimiter=' ', dtype=np.uint8).reshape(h, w, 3)
  pixel_data = np.clip(pixel_data, 0, 255)

  return pixel_data