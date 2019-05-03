"""
 Föreläsning A - Kodexempel 6 ett program som omvandlar
 grader i Celsius till grader i Fahrenheit.
""" 

def main():
    temp_celsius = float(input("Antal grader Celsius tack: "))
    temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)  
    print("Temperaturen i Fahrenheit = ", temp_fahrenheit)

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * (9 / 5.0) + 32
    return fahrenheit
    
main()
