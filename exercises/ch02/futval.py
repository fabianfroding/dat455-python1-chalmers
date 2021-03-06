# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of an investment over a specified number of years.")

    years = eval(input("Enter the number of years: "))
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual(yearly) interest rate: "))
    compound = eval(input("Enter the number of times that the interest is compunded each year: "))
    fixed = eval(input("Enter a fixed amount to invest each year: "))

    for i in range(years):
        for j in range(compound):
            principal = principal * (1 + (apr / compound)) + fixed
            

    print("The value in " + str(years) + " years is:", principal)

main()