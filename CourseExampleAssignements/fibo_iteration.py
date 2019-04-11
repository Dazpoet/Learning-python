#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fibo_iteration(n):
    a = 0
    b = 1

    for i in range(n):
        print("Fibonacci ",i, ": ",a , b)
        b = a + b
        a = b - a

def main():
    user_input = int(input("How many fibonnacinumbers do you want?: "))
    fibo_iteration(user_input)

if __name__ == "__main__":
    main()