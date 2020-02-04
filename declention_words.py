#!/usr/bin/env python
s = ' программист'

def hello(a):
    mod = a % 10
    mod2 = a % 100
    
    if mod == 1 and mod2 != 11:
        return str(a) + s
    elif (mod >= 2 and mod <= 4 and mod2 != 12 and mod2 != 13 and mod2 != 14):
        return str(a)+s+'а'
    else:
        return str(a)+s+'ов'

if __name__ == "__main__": 
    a = int(input())
    print(hello(a))
