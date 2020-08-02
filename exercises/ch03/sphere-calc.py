import math
import sys


def run():
    print("This program calculates the volume and area of a sphere, given it's radius.")
    r = eval(input("Enter radius: "))
    print("Volume: " + str(calcVol(r)))
    print("Area: " + str(calcArea(r)))


def calcVol(r):
    return 4 / 3 * math.pi * (r ** 3)


def calcArea(r):
    return 4 * math.pi * (r ** 2)


run()