# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    print("Welcome to the temperature converter. This program converts degrees in Celsius to Fahrenheit.")

    print('{:<12}'.format("Celsius") + '{:>12}'.format("Fahrenheit"))

    for i in range(1,10):
        celsius = i * 10
        print('{:<12}'.format(celsius) + '{:>12}'.format(9/5 * celsius + 32))

    #for i in range(5):
        #celsius = eval(input("What is the Celsius temperature? "))
        #fahrenheit = 9/5 * celsius + 32
        #print("The temperature is", fahrenheit, "degrees Fahrenheit.")

    input ("Press the <Enter> key to quit.") 

main()