import numpy as np
import math

def getAnalyticModel():
    x = np.linspace(0, 10, 1000000)
    ydc =4/9
    ycosine = (4/9)*np.exp(-2.1*x)*np.cos(math.sqrt(4.59)*x)
    ysine=(1/(15*math.sqrt(4.59)))*np.exp(-2.1*x)*np.sin(math.sqrt(4.59)*x)
    y=ydc-ycosine+ysine
    return (x, y)