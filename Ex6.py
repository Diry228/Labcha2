def MnogoVsego(Vsevmeste):
    Cifri = []
    Bukavki = []
    Other = []

    with open("Vsevmeste.txt", 'r') as file:
        for line in file:
            for char in line:
                if char.isdigit():
                    Cifri.append(char)
                elif char.isalpha():
                    Bukavki.append(char)
                else:
                    Other.append(char)

    print("Цифры:")
    while Cifri:
        print(Cifri.pop(0), end = "")

    print("\nБуквы:")
    while Bukavki:
        print(Bukavki.pop(0),end = "")

    print("\nОстальные символы:")
    while Other:
        print(Other.pop(0), end = "")

Vsevmeste = "Vsevmeste.txt"
MnogoVsego(Vsevmeste)
