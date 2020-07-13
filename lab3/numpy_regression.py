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



def poly(a, x):
    res = 0
    for i in range(len(a)):
        if i == 0:
            #print(a[i])
            res += a[i]
        elif i == 1:
            #print(a[i] * x)
            res += a[i] * x
        else:
            #print(a[i] * pow(x, i))
            res += a[i] * pow(x, i)
    return res
        


def load():
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    measurements = loadtxt(arg1)
    n = int(arg2)
    
    # Convert str to floats
    for i in range(len(measurements)):
        for j in range(len(measurements[i])):
            measurements[i][j] = float(measurements[i][j])
    
    measurements = transpose(measurements)
    X = measurements[0]
    Y = measurements[1]

    Xp  = powers(X, 0, n)
    Yp  = powers(Y, 1, 1)
    Xpt = Xp.transpose()

    a = matmul(linalg.inv(matmul(Xpt, Xp)), matmul(Xpt, Yp))
    a = a[:, 1]

    XMin = min(X)
    XMax = max(X)
    Xn = (XMax - XMin) / 0.2
    X2 = linspace(XMin, XMax, int(Xn)).tolist()

    Y2 = []
    for i in range(len(X2)):
        Y2.append(poly(a, X2[i]))
    
    plt.plot(X, Y,'ro', label="Chirps")
    plt.plot(X2, Y2, label="Predicted")
    plt.legend(loc="upper left")
    plt.show()



load()