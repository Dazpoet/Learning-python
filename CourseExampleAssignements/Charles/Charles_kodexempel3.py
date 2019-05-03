"""
 Charles Babbage - kodexempel 3
 Fibonacciserie genom iteration
 De genererade talen skrivs ut parvis
""" 

def main():
    antal = int(input('Hej, hur många Fibonaccitalpar vill du skriva ut? '))
    fibo_iteration(antal) 


def fibo_iteration(n):
 a = 0
 b = 1
 for i in range(n):
   print('Fibonacci ',i,': ', a, b)
   b = a + b
   a = b - a 
         

if __name__ == "__main__":
    main()


