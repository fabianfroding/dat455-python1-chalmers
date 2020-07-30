# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    print("Welcome to the temperature converter. This program converts degrees in Celsius to Fahrenheit.")

    print('{:<12}'.format("Fahrenheit") + '{:>12}'.format("Celsius"))

    for i in range(1,10):
        fahrenheit = i * 10
        print('{:<12}'.format(fahrenheit) + '{:>12}'.format(((fahrenheit - 32) * 5) / 9))

    #for i in range(5):
        #celsius = eval(input("What is the Celsius temperature? "))
        #fahrenheit = 9/5 * celsius + 32
        #print("The temperature is", fahrenheit, "degrees Fahrenheit.")

    input ("Press the <Enter> key to quit.") 

main()