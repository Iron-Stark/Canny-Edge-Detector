'''
  File name: edgeLink.py
  Author: Dewang Sultania
  Date created: 09/21/2018
'''

'''
  File clarification:
    Use hysteresis to link edges based on high and low magnitude thresholds
    - Input M: H x W logical map after non-max suppression
    - Input Mag: H x W matrix represents the magnitude of gradient
    - Input Ori: H x W matrix represents the orientation of gradient
    - Output E: H x W binary matrix represents the final canny edge detection map
'''
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
import numpy as np
import collections
import time
import matplotlib.pyplot as plt

visited = set()
def check(E,i,j):
    if i<E.shape[0] and j<E.shape[1] and i>=0 and j>=0:
        return True
    return False

def bfs(E,i,j, threshold_low, threshold_high):
    queue = collections.deque([(i,j)])
    while queue:
        point = queue.popleft()
        for k in range(8):
            new_i = point[0]+dx[k]
            new_j = point[1]+dy[k]
            if check(E, new_i, new_j):
                if(new_i,new_j) not in visited and E[new_i,new_j]!=-1:
                        visited.add((new_i,new_j))
                        queue.append((new_i,new_j))
                        E[new_i,new_j] = 1
    return E

def edgeLink(M, Mag, Ori):
  # TODO: your code here
  start = time.time()
  M = M*Mag
  M = ((M-M.min())*255)/(M.max()-M.min())
  E = np.zeros(M.shape)
  threshold_low = M.mean()*2+ np.var(M)/100
  threshold_high = M.mean()*6 + np.var(M)/100
  E[M > threshold_high] = 1
  E[M < threshold_low] = -1
  starts = np.argwhere(E==1)
  for i in range(starts.shape[0]):
      [x,y] = starts[i]
      if ((x,y) not in visited):
          E = bfs(E,x,y,threshold_low, threshold_high)
  E[np.logical_and(np.not_equal(E,0), np.not_equal(E,1))] = 0
  end = time.time()
  print("The time taken by Edge Linking for this image is {} seconds".format(end-start))
  return E
