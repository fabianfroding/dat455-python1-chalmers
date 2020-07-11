import sys
import matplotlib.pyplot as plt
from numpy import *



def powers(list, num1, num2):
    if len(list):
        rows = len(list)
        cols = num2 + 1
        mat = [[0 for x in range(cols)] for y in range(rows)]

        for i in range(0, rows):
            for j in range(num1, cols):
                mat[i][j] = pow(list[i], j)

        return array(mat)
    return array([])



def load():
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    measurements = loadtxt(arg1)
    n = arg2
    
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
    m1Invert = linalg.pinv(m1)
    b, m = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))

    Y2 = []
    for i in range(len(X)):
        Y2.append(b[1] + m[1] * X[i])
    
    plt.plot(X, Y)
    plt.plot(X, Y,'ro', label="Chirps")
    plt.plot(X, Y2, label="Predicted")
    plt.legend(loc="upper left")
    plt.show()



load()