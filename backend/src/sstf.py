from heapq import *

def sstf(arm_position, lrequests, debug=False):
  """
  Shortest Seek Time First implementation

  Args:
      arm_position (int): arm position
      lrequests (list<int>): request list
  """
  time=0
  n = len(lrequests)
  current_pos=arm_position
  
  while len(lrequests) > 0:
    minDist = float('INF')  
    closest = -1
    for i in range(len(lrequests)):
        if abs(current_pos-lrequests[i]) < minDist:
            minDist = abs(current_pos-lrequests[i])
            closest = i
    a_request = lrequests[closest]
    time += abs(a_request-current_pos)
    current_pos=a_request
    lrequests.pop(closest)
    if debug: print("> ", current_pos ,"seeked")
  
  aveg=time / n
  return aveg

print(sstf(40, [50, 60, 20], True))
