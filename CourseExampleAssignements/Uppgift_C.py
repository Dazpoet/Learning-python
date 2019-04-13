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

    #More fun method
    #hogsta = 0
    #for i in range(0, len(lista) - 1):
    #    if i > hogsta:
    #        hogsta = i
    #    else:
    #        continue

    #return hogsta

def minvarde(lista):
    lista.sort()

    minvarde = lista[0]

    return minvarde

    #More fun method
    #minimi = lista[0]
    #for i in range(1,len(lista) -1):
        #if i < minimi:
            #minimi = i
    #else:
        #continue


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
    
    collect_data = True 
    while collect_data:
        try:
            nytt_varde = int(input("\nAnge ett heltal: "))
            lista.append(nytt_varde)
            if len(lista) == 10:
                collect_data = False
        except ValueError:
            print("Höruduru, ingenting annat än heltal är ok här!")

    print(f"\nSumman av dina värden är {summa(lista)}\n")

    print(f"Medelvärdet av du förde in var {round(medel(lista), 2)}\n")
    
    print(f"Det största talet du matade in var {maxvarde(lista)}\n")

    print(f"Det minsta talet du matade in var {minvarde(lista)}\n")

    print(f"Medianen av dina inmatade värden är {median(lista)}\n")

if __name__ == "__main__":
    main()