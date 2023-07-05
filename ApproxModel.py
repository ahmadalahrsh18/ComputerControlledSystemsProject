import numpy as np
import math

def getApproxModel(Tsim,Tsampling):
    x=[[0],[0]]
    n=int(Tsim/Tsampling)
    timeAxis=[0]
    for i in range(n):
        x1k=x[0][i]
        x2k=x[1][i]
        
        x1k1=x1k+Tsampling*x2k+Tsampling
        x2k1=-9*Tsampling*x1k+(1-4.2*Tsampling)*x2k-0.2*Tsampling
        x[0].append(x1k1)
        x[1].append(x2k1)
        timeAxis.append((i+1)*Tsampling)
    return (timeAxis,x[0])
        