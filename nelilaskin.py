
operaatio = input("Valitse operaatio (+, -, *, /):")
if operaatio != "+" and operaatio != "-" and operaatio != "*" and operaatio != "/":
    print("Operaatiota ei ole olemassa")
else:
    try:
        luku_1 = float(input("Anna luku 1:"))
        luku_2 = float(input("Anna luku 2:"))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        if operaatio == "+":
            summa = luku_1 + luku_2
            print(summa)
        elif operaatio=="-":
            summa = luku_1 - luku_2
            print(summa)
        elif operaatio == "*":
            summa = luku_1 * luku_2
            print(summa)
        elif operaatio == "/":
            summa = luku_1 / luku_2
            print(summa)