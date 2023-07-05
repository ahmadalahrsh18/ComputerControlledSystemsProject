import math

def getPointInAnalyticalModel(t):
    ydc =4/9
    ycosine = (4/9)*math.exp(-2.1*t)*math.cos(math.sqrt(4.59)*t)
    ysine=(1/(15*math.sqrt(4.59)))*math.exp(-2.1*t)*math.sin(math.sqrt(4.59)*t)
    return ydc-ycosine+ysine