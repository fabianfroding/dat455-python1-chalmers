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

        return mat
    return array([])



def load(file):
    measurements = loadtxt(file)

    measurements = transpose(measurements)
    X = measurements[0]
    Y = measurements[1]
    
    # Convert str to floats
    for i in range(len(measurements)):
        for j in range(len(measurements[i])):
            measurements[i][j] = float(measurements[i][j])
    print(measurements)

    Xp  = powers(X,0,1)
    Yp  = powers(Y,1,1)
    Xpt = transpose(Xp)

    m1 = matmul(Xpt, Xp)
    #print(m1)
    m2 = matmul(Xpt, Yp)
    print(m2)
    m2Invert = linalg.inv(m2)
    #[[b],[m]] = matmul(invert(matmul(Xpt, Xp)), matmul(Xpt, Yp))



load("chirps.txt")