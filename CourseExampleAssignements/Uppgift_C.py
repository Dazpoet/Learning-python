#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def summa(lista):
    summa = 0
    for i in range(0,len(lista)):
        summa += lista[i]
    
    return summa

def maxvarde(lista):
    lista.sort()

    maxvarde = lista[len(lista) - 1]

    return maxvarde

def minvarde(lista):
    lista.sort()

    minvarde = lista[0]

    return minvarde

def medel(lista):
    medel = summa(lista) / len(lista)

    return medel

def median(lista):
    lista.sort()

    if len(lista) % 2 == 0:
        mittenvarde_index = int((len(lista) / 2) - 1)
        median = lista[mittenvarde_index]

        return median
    else:
        mittenvarde_index_1 = math.floor(len(lista)/2)
        mittenvarde_index_2 = math.ceil(len(lista)/2)
        
        median = (lista[mittenvarde_index_1] + lista[mittenvarde_index_2]) / 2
        return median

def main():

    lista = []
    
    while len(lista) < 11:
        try:
            nytt_varde = int(input("\nAnge ett heltal: "))
            lista.append(nytt_varde)
        except ValueError:
            print("Höruduru, ingenting annat än heltal är ok här!")

    print(f"\nSumman av dina värden är {summa(lista)}\n")

    print(f"Medelvärdet av du förde in var {round(medel(lista), 2)}\n")
    
    print(f"Det största talet du matade in var {maxvarde(lista)}\n")

    print(f"Det minsta talet du matade in var {minvarde(lista)}\n")

    print(f"Medianen av dina inmatade värden är {median(lista)}\n")

if __name__ == "__main__":
    main()