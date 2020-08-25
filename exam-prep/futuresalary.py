


def main():
    print("Welcome to the Future Salary Predictor.")

    current = eval(input("Enter your current salary: "))
    increment = eval(input("Enter the yearly precentage increase: "))
    years = eval(input("Enter the number of years: "))

    future = current
    for i in range (1, years + 1):
        future = future * (1 + (increment * 0.01))
        print("Your future salary after " + str(i) + " years will be " + str(future) + " SEK")

main()