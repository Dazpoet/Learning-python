#Ada - kodexempel 2: variabler, konstanter och funktioner 

radie = 7 #variabel vilket visas genom att vi använder gemener
PI = 3.14159265 #konstant vilket alltid skrivs med VERSALER
  
#funktionsdefinition
def visa_cirkelns_omkrets (radie, PI): 
    omkrets = 2 * PI * radie
    print("Cirkelns omkrets: ", omkrets)

#funktionsanrop
visa_cirkelns_omkrets(radie, PI)
    
