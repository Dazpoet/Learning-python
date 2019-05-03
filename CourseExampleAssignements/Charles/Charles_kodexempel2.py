"""
 Charles Babbage - kodexempel 2
 Att beräkna summan av en lista
""" 

min_lista = [7, 19, 8, 11, 14, 9]

def main():
    summa = 0
    for i in range(0,len(min_lista)):
        summa += min_lista[i]
    print(summa)    

if __name__ == "__main__":
    main()


