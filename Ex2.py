from collections import deque

deck = deque('абвгдежзийклмнопрстуфхцчшщъыьэюя')
with open('what.txt', 'r') as file:
    encrypt = file.read()

decrypt = ""
for char in encrypt:
    if char in deck:
        decrypt+= deck[(deck.index(char) - 1)]
print(decrypt)