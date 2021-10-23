try:
    temp = input("enter temperature: ")
    temp = temp.split()
    if temp[1] == "C":
        print("{} degree Celsius converted to Fahrenheit is: ".format(temp[0]), end = "")
        print(int(temp[0]) * (9/5) + 32, "F")
    if temp[1] == "F":
        print("{} degree Fahrenheit converted to Celsius is: ".format(temp[0]), end="")
        print((int(temp[0]) - 32) * 5/9, "C")
except:
    print("enter the temperature with notation at the end ")