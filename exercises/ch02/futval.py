# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of an investment over a specified number of years.")

    years = eval(input("Enter the number of years: "))
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in " + str(years) + " years is:", principal)

main()