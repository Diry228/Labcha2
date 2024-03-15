from collections import deque
def rightScobki(Scobki):
    deque1 = deque()
    with open("ScobkiKub.txt", 'r') as file:
        for line in file:
            for char in line:
                if char == '[':
                    deque1.append('[')
                else:
                    if char == ']':
                        if not deque1:
                            return False
                        deque1.pop()

    return len(deque1) == 0

Scobki = "ScobkiKub.txt"
if rightScobki(Scobki):
    print("Победа")
else:
    print("Неудача")