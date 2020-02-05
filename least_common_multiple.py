#!/usr/bin/env python

x = int(input())
y = int(input())

def gcm(n, m):
    while 1:
        if n > m:
            m, n = n, m
        r = m % n

        if r == 0:
            return n
        else:
            m, n = n, r

print(int((x*y)/gcm(x, y)))
