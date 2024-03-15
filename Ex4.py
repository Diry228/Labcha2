def rightScobki(Scobki):
    stack = []
    with open("Scobki.txt", 'r') as file:
        for line in file:
            for char in line:
                if char == '(':
                    stack.append('(')
                else:
                    if char == ')':
                        if not stack:
                            return False
                        stack.pop()

    return len(stack) == 0

Scobki = "Scobki.txt"
if rightScobki(Scobki):
    print("Победа")
else:
    print("Неудача")