from vacuum import *

res = []
state = []
for i in range(8) :
    state.clear()
    res.clear()
    s = i & 1
    if s == 0:
        state.append('Clean')
    else:
        state.append('Dirty')
    s = i & 2
    if s == 0:
        state.append('Clean')
    else:
        state.append('Dirty')
    s = i & 4
    if s == 0:
        state.append(0)
    else:
        state.append(1)
    print('Initial State: ',state,res)
    actSeq, steps = vacuum(state,res)  
    print(actSeq,steps,sep=',')
