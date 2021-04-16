while True:
    try:
        x = float(input("Bitte eine Zahl eingeben:"))
        inverse = 1.0 / x
        print(inverse)
    except ValueError:
        print ("Entweder einen int oder einen float eingeben")
    except ZeroDivisionError:
        print("Infinity")
    finally:
        print("Das ist das Finale")
        if(input("Ende mit q - weiter mit jeder anderen Taste: ")=="q"):
            break

print("Und nun ist das Programm zu Ende")

