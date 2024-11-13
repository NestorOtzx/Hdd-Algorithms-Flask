
def fcfs(arm_position, lrequests, debug=False):
  """
  First Come First Serve implementation

  Args:
      arm_position (int): arm position
      lrequests (list<int>): request list
  """
  time=0
  n=len(lrequests)
  current_pos=arm_position
  for a_request in lrequests:
    time += abs(a_request-current_pos)
    current_pos=a_request
    if debug: print("> ", current_pos ,"seeked")
  
  aveg=time / n
  return aveg