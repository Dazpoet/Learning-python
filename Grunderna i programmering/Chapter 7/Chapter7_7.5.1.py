#!/usr/bin/env python3
#Take input from the user in celsius, convert to Fahrenheit and
#use if logic to give feedback regarding the temperature

def main():
    temp_celsius = float(input("What is the temperature in Celsius?: "))
    f = convert_celsius_to_fahrenheit(temp_celsius)
    if f > 80:
        print("It's hot outside with a temperature of " + str(f) + " degrees F")
    elif f < 40:
        print("It's cold outside with a temperature of " + str(f) + " degrees F")
    else:
        print("It's " + str(f) + " degrees F outside")

def convert_celsius_to_fahrenheit(temp_celsius):
    temp_fahrenheit = temp_celsius * 1.8 + 32
    return temp_fahrenheit

main()