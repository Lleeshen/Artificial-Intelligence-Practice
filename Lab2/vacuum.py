def vacuum(state,res):
  try:
    model = state[:2]
    pos = state[2]
  except:
    return ['Error'],-1
  steps = 0
  while model[0] == 'Dirty' or  model[1] == 'Dirty' :
    steps = steps + 1
    if model[pos] == 'Dirty':
      model[pos] = 'Clean'
      res.append('Suck')
    elif pos == 1 :
      pos = 0
      res.append('Left')
    else :
      pos = 1
      res.append('Right')

  return res,steps
