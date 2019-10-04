from vacuum import *

actSeq1,steps1 = vacuum(['Clean','Clean',1],[])
print(actSeq1,steps1)
actSeq2,steps2 = vacuum(['Clean','Dirty',0],[])
print(actSeq2,steps2)
actSeq3,steps3 = vacuum(['Dirty','Dirty',1],[])
print(actSeq3,steps3)

