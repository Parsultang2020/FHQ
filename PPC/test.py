#!/usr/bin/env python3
i = 0
k = 0
while k < 9125:
    i += 1
    print(i, end='')
    if i < 10:
        k += 1
    elif i < 100:
        k += 2
    elif i < 1000:
        k += 3
    else:
        k += 4
input()

