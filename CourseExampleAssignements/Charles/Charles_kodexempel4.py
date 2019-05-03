"""
 Charles Babbage - kodexempel 4
 Fibonacciserie genom rekursion
""" 

def main():
    antal = int(input('Hej, hur många Fibonaccital vill du skriva ut? '))
    print('Fibonacciserien från 0 till ', antal, ': ')
    for i in range(antal):
        print(fibo_rekursiv(i))
 


def fibo_rekursiv(n):
    if n <= 1:
        return n
    else:
        return fibo_rekursiv (n - 1) + fibo_rekursiv ( n - 2)
         

if __name__ == "__main__":
    main()


