def find_missing(list1,list2):
  """" Checks whether a number exists another lists and returns the extra number"""
  a = 0
  if list1 == list2:
    return 0
  
  
  for i in list1:
    if i not in list2:
      a = i
  
  for i in list2:
    if i not in list1:
      a = i
      
  return a