try:
    temp = input("Input the  temperature you like to convert? (e.g., 45F, 102C, 65K etc.) : ")
    degree = int(temp[:-1])
    i_convention = temp[-1]

    #Celsius to Kelvin & Fahrenheit
    if i_convention.upper() == "C":
        print(degree + 273.15,"K")
        print((degree * 9/5)+32,"°F")
    #Fahrenheit to Celsius & Kelvin 
    elif i_convention.upper() == "F":
        print((degree - 32) * 5/9,"°C")
        print((degree - 32) * 5/9 + 273.15,"K")
    #Kelvin to Fahrenheit & Celsius 
    elif i_convention.upper() == "K":
        print((degree - 273.15) * 9/5 + 32,"°F")
        print(degree - 273.15,"°C")
    else:
        print("Input proper convention.")
except:
    print("Input proper convention.")