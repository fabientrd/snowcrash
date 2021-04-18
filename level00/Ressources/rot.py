#!/usr/bin/python3

import sys

a = 1
while a < 26:
    for i in sys.argv[1]:
        ch = ord(i) + a
        if ch > 122:
            ch -= 26
        print(chr(ch), end="")
    print('')
    a += 1
