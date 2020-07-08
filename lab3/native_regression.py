from matrix import *

def load(file):
    measurements = loadtxt(file)

    measurements = transpose(measurements)
    X = measurements[0]
    Y = measurements[1]

    # Not tested
    Xp  = powers(X,0,1)
    Yp  = powers(Y,1,1)
    Xpt = transpose(Xp)

    [[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))



load("chirps.txt")