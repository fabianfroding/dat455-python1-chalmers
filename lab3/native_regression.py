import sys
import matplotlib.pyplot as plt
from matrix import *



def load():
    arg1 = sys.argv[1]
    measurements = loadtxt(arg1)
    
    # Convert str to floats
    for i in range(len(measurements)):
        for j in range(len(measurements[i])):
            measurements[i][j] = float(measurements[i][j])
    
    measurements = transpose(measurements)
    X = measurements[0]
    Y = measurements[1]

    Xp  = powers(X, 0, 1)
    Yp  = powers(Y, 1, 1)
    Xpt = transpose(Xp)

    m1 = matmul(Xpt, Xp)
    m2 = matmul(Xpt, Yp)
    # [[b], [m]] produces "too many values to unpack".
    # Using below method instead and then b[1], m[1], to get correct values.
    b, m = matmul(invert(matmul(Xpt, Xp)), matmul(Xpt, Yp))

    Y2 = []
    for i in range(len(X)):
        Y2.append(b[1] + m[1] * X[i])
    
    plt.plot(X, Y)
    plt.plot(X, Y,'ro', label="Chirps")
    plt.plot(X, Y2, label="Predicted")
    plt.legend(loc="upper left")
    plt.show()



load()