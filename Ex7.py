from collections import deque

def Perebor(Chiferki):
    Ploxie = deque()
    Good = deque()

    with open("Chiferki.txt", 'r') as file:
        for line in file:
            numbers = map(int, line.split())
            for number in numbers:
                if number < 0:
                    Ploxie.append(number)
                else:
                    Good.append(number)
    while Ploxie:
        print(Ploxie.popleft(),end = " ")
    while Good:
        print(Good.popleft(), end = " ")
Chiferki= "Chiferki.txt"
Perebor(Chiferki)