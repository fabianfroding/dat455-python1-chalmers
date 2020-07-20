# File: chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    n = eval(input("How many numbers should I print? "))
    x = eval(input("Enter a number between 0 and 1 (for column 1): "))
    y = eval(input("Enter a number between 0 and 1 (for column 2): "))

    print('{:<8}'.format("input") + '{:^12}'.format(x) + '{:>12}'.format(y))
    print("---------------------------")

    for i in range(n):
        #x = 3.9 * x * (1 - x)
        #x = 3.9 * (x - x * x)
        x = 3.9 * x - 3.9 * x * x

        y = 3.9 * y * (1 - y)

        #print("     " + str(x) + "  " + str(y))
        print('{:<10}'.format("") + '{:^12}'.format(round(x,6)) + '{:>12}'.format(round(y, 6)))

main()