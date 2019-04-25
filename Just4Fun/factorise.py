#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def find_factors(x):
    list_of_factors = []
    for i in range(1, x+1):
        if x % i == 0:
            list_of_factors.append(i)

    return list_of_factors
    
def main():
    num = int(input("Ge mig ett tal att faktorisera: "))
    factors = find_factors(num)
    print(factors)

if __name__ == "__main__":
    main()