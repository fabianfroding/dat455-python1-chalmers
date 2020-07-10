import sys
import matplotlib.pyplot as plt
#from matrix import *
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
    measurements = loadtxt(arg1)
    
    # Convert str to floats
    for i in range(len(measurements)):
        for j in range(len(measurements[i])):
            measurements[i][j] = float(measurements[i][j])
    
    measurements = transpose(measurements)
    X = measurements[0]
    Y = measurements[1]

    Xp  = powers(X, 0, 1)
    print(Xp)
    Yp  = powers(Y, 1, 1)
    print(Yp)
    Xpt = transpose(Xp)
    print(Xpt)

    m1 = matmul(Xpt, Xp)
    print(m1)
    m2 = matmul(Xpt, Yp)
    print(m2)
    m1Invert = linalg.pinv(m1)
    print(m1Invert)
    te = matmul(linalg.pinv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    print(te)
    #[[b],[m]] = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))



load()