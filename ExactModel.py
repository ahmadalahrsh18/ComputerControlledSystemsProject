import math;
import numpy as np
def getExactModel(Tsim,Tsampling):
    w= math.exp(-2.1*Tsampling)*math.cos(math.sqrt(4.59)*Tsampling)
    a = (1/(math.sqrt(4.59)))*math.exp(-2.1*Tsampling)*math.sin(math.sqrt(4.59)*Tsampling)
    A= np.array([[0,1], [-9,-4.2]])
    invA =np.linalg.inv(A)
    phi=np.array([[w+2.1*a,a],[-9*a, w-2.1*a]])

    theta=np.matmul(np.matmul(invA,phi-np.eye(2)),np.array([[1],[-0.2]]))
    
    timeAxis = np.arange(0,Tsim, Tsampling)
    
    y = []
    x = np.array([[0],[0]])
    u = np.array([[1]]) # input step
    for _ in timeAxis:
        x = np.matmul(phi, x) + np.matmul(theta, u)
        y_value = np.matmul(np.array([[1,0]]), x) 
        y.append(y_value.squeeze())
    return (timeAxis,y)
