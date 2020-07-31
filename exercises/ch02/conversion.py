

def isFourDigit(s):
    if (len(s) != 4):
        print("Input is not four digits. Program terminated.")
        return False
    return True



def isBinary(s):
    for i in range(len(s)):
        if (s[i] != "1" and s[i] != "0"):
            print(s + " is not a binary number. Program terminated.")
            return False
    return True



def conversion():
    print("This program converts a four-digit binary number to a integer number.")
    bin = str(eval(input("Enter a four-digit binary number: ")))

    # Validate input
    if (not isFourDigit(bin) and not isBinary(bin)):
        return

    # TODO: Fix leading zeros error

    # Calculate int value
    val = 0
    multiplier = 1
    binLen = len(bin)
    for i in range(binLen):
        val += int(bin[binLen - 1 - i]) * multiplier
        multiplier *= 2

    return str(val)


print(conversion())