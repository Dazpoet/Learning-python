def odd_or_even():
    try:
        user_input = int(input("Ge mig ett heltal: "))
        if user_input % 2 == 0:
            print("Talet är jämnt")
        else:
            print("Talet är ojämnt")
    except ValueError:
        print("Det var inte ett heltal")
        odd_or_even()

odd_or_even()