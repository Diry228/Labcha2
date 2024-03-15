def Obmen(vvod, vivod):
    stack = []

    with open("vvod.txt", 'r') as file:
        for line in file:
            stack.append(line)

    with open("viviod.txt", 'w') as file:
        while stack:
            file.write(stack.pop() + "\n")

vvod = "vvod.txt"
vivod = "viviod.txt"
Obmen(vvod, vivod)
