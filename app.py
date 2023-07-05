import matplotlib.pyplot as plt
import math
import numpy as np

from AnalyticModel import getAnalyticModel
from ApproxModel import getApproxModel
from ExactModel import getExactModel
from ISE import ISE

Tsamples =[0.01,0.1,0.5]

    



for i in Tsamples:
    plt.figure()
    plt.suptitle(i)

    (x,y) = getAnalyticModel()
    plt.subplot(211)
    plt.plot(x, y,color='g',label='Analytic Model Response')
    plt.xlabel("time")
    plt.ylabel("amplitude")

    (xapprox,yapprox) = getApproxModel(10,i)
    plt.subplot(211)
    plt.plot(xapprox, yapprox,label='Approx Model Response')
    plt.xlabel("time")
    plt.ylabel("amplitude")


    (xapprox1,yapprox1) = getExactModel(10,i)
    plt.subplot(211)
    plt.plot(xapprox1, yapprox1,color='k',label='Exact Model Response')
    plt.xlabel("time")
    plt.ylabel("amplitude")
    plt.title("The response of the System")
    plt.legend()

    errors = ISE(yapprox,i)
    plt.subplot(212)
    plt.plot(xapprox, errors,color='r',label='Error of Approx Model')
    plt.xlabel("time")
    plt.ylabel("error")
    
    
    errors = ISE(yapprox1,i)
    plt.subplot(212)
    plt.plot(xapprox1, errors,color='m' ,label='Error of Exact Model' )
    plt.xlabel("time")
    plt.ylabel("error")
    plt.title("The error between the Approx and Exact Models against Analytical Model responces")
    plt.legend()

plt.show()
