from collections import deque

with open('Book.txt', 'r') as fileread:
    lines = fileread.readlines()

deq1 = deque(sorted(lines))
deq2 = deque()
while deq1:
    deq2.append(deq1.pop())
while deq2:
    print(deq2.pop())
