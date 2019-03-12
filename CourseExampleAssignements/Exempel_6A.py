#!/usr/bin/env python3

def dividera(c, d):
    try:
        kvot = c/d
        return str(c) + '/' + str(d) + '=' + str(kvot)
    except ZeroDivisionError:
        return "FEEBLE BEING Y U DIVIDE BY NOTHING?!"

def user_input():
    while True:
        try:
            dividend = int(input("Gief dividend!: "))
            divisor = int(input("Gief divisor!: "))
            return dividera(dividend, divisor)
        except ValueError:
            print("Y U NO INT?!")

def main():
   f = user_input()
   print(f)

if __name__ == '__main__':
    main()