import math
from AnalyticalPoint import getPointInAnalyticalModel

def ISE(yapprox,Tsampling):
    n = len(yapprox)
    summedArea=0
    summedAreaVector=[]
    for i in range(n):
            error = getPointInAnalyticalModel(i*Tsampling)-yapprox[i]
            error2 = math.pow(error,2)
            summedArea = summedArea + error2*Tsampling
            summedAreaVector.append(summedArea)

    return summedAreaVector