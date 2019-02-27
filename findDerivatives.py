'''
  File name: findDerivatives.py
  Author: Dewang Sultania
  Date created: 09/21/2018
'''

'''
  File clarification:
    Compute gradient information of the input grayscale image
    - Input I_gray: H x W matrix as image
    - Output Mag: H x W matrix represents the magnitude of derivatives
    - Output Magx: H x W matrix represents the magnitude of derivatives along x-axis
    - Output Magy: H x W matrix represents the magnitude of derivatives along y-axis
    - Output Ori: H x W matrix represents the orientation of derivatives
'''
from utils import GaussianPDF_2D
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import time
def findDerivatives(I_gray):
  # TODO: your code here
  start = time.time()
  gaussianKernel = GaussianPDF_2D(0,1,7,7)
  dx = np.array([1,-1]).reshape(1,2)
  dy = np.array([1,-1]).reshape(2,1)
  Gx = signal.convolve2d(gaussianKernel, dx, mode = 'same')
  Gy = signal.convolve2d(gaussianKernel, dy, mode = 'same')
  Magx = signal.convolve2d(I_gray, Gx, mode = 'same')
  Magy = signal.convolve2d(I_gray, Gy, mode = 'same')
  Mag = np.sqrt(Magx**2 + Magy**2)
  Ori = np.arctan2(Magy, Magx)
  end = time.time()
  print("Time taken to calculate the gradients for this image = {} seconds".format(end-start))
  return Mag, Magx, Magy, Ori
