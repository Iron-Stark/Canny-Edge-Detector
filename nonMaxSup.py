'''
  File name: nonMaxSup.py
  Author: Dewang Sultania
  Date created: 09/21/2018
'''

'''
  File clarification:
    Find local maximum edge pixel using NMS along the line of the gradient
    - Input Mag: H x W matrix represents the magnitude of derivatives
    - Input Ori: H x W matrix represents the orientation of derivatives
    - Output M: H x W binary matrix represents the edge map after non-maximum suppression
'''

from scipy.interpolate import RectBivariateSpline
import time
import numpy as np
def nonMaxSup(Mag, Ori):
  # TODO: your code here
    start = time.time()
    x = range(Mag.shape[0])
    y = range(Mag.shape[1])
    M = Mag.copy()
    xx,yy = np.meshgrid(y,x)
    interp2d = RectBivariateSpline(x,y,M)
    posgradX = xx+np.cos(Ori)
    posgradY = yy-np.sin(Ori)
    neggradX = xx-np.cos(Ori)
    neggradY = yy+np.sin(Ori)
    posgrad = interp2d.ev(posgradY, posgradX)
    neggrad = interp2d.ev(neggradY, neggradX)
    M[np.less_equal(M,posgrad) | np.less_equal(M,neggrad)] = 0
    M[M!=0] = 1
    end = time.time()
    print("Time taken for non maximal supression on the image = {} seconds".format(end-start))
    return M
