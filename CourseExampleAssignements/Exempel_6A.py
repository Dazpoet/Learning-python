#!/usr/bin/env python3

def dividera(c, d):
    try:
        kvot = c/d
        return str(c) + '/' + str(d) + '=' + str(kvot) #This will be put into f when a proper division is performed
    except ZeroDivisionError:
        return "FEEBLE BEING Y U DIVIDE BY NOTHING?!" #This will be put into f when a ZeroDivisionError is thrown

def user_input():
    while True:
        try:
            dividend = int(input("Gief dividend!: "))
            divisor = int(input("Gief divisor!: "))
            return dividera(dividend, divisor)
        except ValueError:
            print("Y U NO INT?!") #Don't mix print and return unless there's a good reason for it

def main():
   f = user_input()
   print(f)

if __name__ == '__main__':
    main()