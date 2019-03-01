#!/usr/bin/env python3

#Assignement:
# Create a program that accepts a float as input and then convert it from km/h to m/s or vice versa
# Have a menu that allows the user to choose between the two function and contains enough information
#for a good user experience
# Print the answers with 2 decimals
# Use try-except when applicable
# Have fun!

import time

vac_speed_of_light_mps = 299792458 #Speed of light in metres per second. We want to warn anyone who moves faster than this

def convert_kmph_to_mps(): #Asks for user input and then converts kilometres per hour to metres per second
    try:
        kmph = float(input("Hur många km/h vill du konvertera till m/s? "))
        mps = round(kmph / 3.6, 2) #Converts and rounds to 2 decimals
        if mps > vac_speed_of_light_mps:
            warp_speed(mps)
            print("\nMed den varningen sagd så är " + str(kmph) + " km/h samma sak som " + str(mps) + " m/s.\n")
        else:
            print("\n" + str(kmph) + " km/h är samma sak som " + str(mps) + " m/s.\n")
    except ValueError: #Catch when an incorrectly formatted value is written or when letters are used
        print("Du måste ange en hastighet med hjälp av siffor, kom ihåg att använda dig av \".\" som skiljetecken.\n")
    except: #Quit gracefully when unforseen exceptions are thrown and inform the user on how to report them
        critical_error()

def convert_mps_to_kmph(): #Asks for user input and then converts metres per second to kilometres per hour
    try:
        mps = float(input("Hur många m/s vill du konvertera till km/h? "))
        kmph = round(mps * 3.6, 2) #Converts and rounds to 2 decimals
        if mps > vac_speed_of_light_mps:
            warp_speed(mps)
            print("\nMed den varningen sagd så är " + str(mps) + " m/s samma sak som " + str(kmph) + " km/h.\n")
        else:
            print("\n" + str(mps) + " m/s är samma sak som " + str(kmph) + " km/h.\n")
    except ValueError: #Catch when an incorrectly formatted value is written or when letters are used
        print("Du måste ange en hastighet med hjälp av siffor, kom ihåg att använda dig av \".\" som skiljetecken.\n")
    except: #Quit gracefully when unforseen exceptions are thrown and inform the user on how to report them
        critical_error()

def warp_speed(mps): #We call this when people move faster than light
    diff = round(mps - vac_speed_of_light_mps, 2)
    print("\nFörhoppningsvis är hastigheten du matade in inte en del av en större beräkning?\n\
Din hastighet är " + str(diff) + " m/s högre än ljusets hastighet i vakuum och så fort kan inget känt föremål röra sig.\n\
Om du har gjort korrekta beräkningar och/eller stött på något som rör sig så här fort rekommenderar jag att du kontaktar ESA")

def critical_error(): #We call this when an unknown exception is thrown
    print("""Någonting gick väldigt fel. Om felet är möjligt att reproducera vänligen skapa ett ärende på följande sida:\n https://github.com/Dazpoet/Learning-python/issues""")
    print("Programmet avslutas om: ")
    
    counter = 5
    while counter > 0: #Give the user a few seconds to consider the error before quitting, prevents window from closing prematurely
        print(counter)
        time.sleep(1)
        counter -= 1
    
    quit()

def easter_egg(): #Easter egg for the initiated
    print ("\n\nDu hittade den magiska Dazrullen!")
    print("""              _
  .--""--.___.._
 (  <__>  )     `-.
 |`--..--'|      <|
 |       :|       /
 |       :|--""-./
 `.__  __;' o!O
     ""     

------------------------------------------------
This ASCII art was fetched from http://www.ascii-art.de/ascii/t/toiletpaper.txt
Artist: Ojoshiro

If you are the copyright-holder of this art and would like it removed please open an issue at:
https://github.com/Dazpoet/Learning-python/issues and it will be removed with due haste.
""")

def main(): #Open a menu and call relevant functions depending on the choice made
    
    menu = True
    
    print("""\nVälkommen till Willes enhetskonverterare!\n\n\
Med detta smarta program behöver du aldrig igen oroa dig över hur man konverterar mellan km/h och m/s eftersom programmet gör det åt dig.\n""")
    
    while menu:
        try:
            answer = int(input("""Vad vill du göra?
            1. Konvertera km/h till m/s
            2. Konvertera m/s till km/h
            3. Avsluta programmet
            """))
            if answer == 1:
                convert_kmph_to_mps()
            elif answer == 2:
                convert_mps_to_kmph()
            elif answer == 3:
                menu = False
            elif answer == 99:
                easter_egg()
            else:
                print("Du måste ange 1, 2 eller 3 för att komma vidare\n")
        except ValueError:
            print("""Du måste ange en siffra: helst 1, 2 eller 3 men kanske finns det ett fjärde alternativ?\nMan kan aldrig vara riktigt hundra...\n""")
        except:
            critical_error()

main()