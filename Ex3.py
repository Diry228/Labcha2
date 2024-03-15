def hanoi(n, start, end, help):
    if n == 1:
        print(f"перенести со стержня {start} на стержень {end}")
    else:
        hanoi(n-1, start, help, end)
        print(f"перенести со стержня {start} на стержень {end}")
        hanoi(n-1, help, end, start)

with open('diski.txt', 'r') as file:
    n = int(file.read())
print("Количество дисков равно: ",n)
hanoi(n, 1, 3, 2)
#print("Все диски были переставлены на стержень: ", 3)