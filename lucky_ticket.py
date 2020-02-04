#!/usr/bin/env python

n = str(input('Enter your ticket number:'))
fHalf = sum([int(x) for x in n[:3]])
sHalf = sum([int(x) for x in n[3:]])

if fHalf == sHalf:
    print('Счастливый')
else: 
    print('Обычный')
