while True:
    try:
        c = float(input("what's the temperature in celsius? "))

        f = c * 9 / 5 + 32

        print("your temperature in freedom units is", f)

        cont = input("Do you want to continue (Y/N)?")
        if cont.upper() == "N":
            break
    except ValueError:
        print("It is not a numerical value")
