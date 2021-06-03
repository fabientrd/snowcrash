#!/usr/bin/python

import sys

f = open(sys.argv[1], "r")
s = f.read()
ret = ""
i = 0
while i < len(s) - 1:
    print(ord(s[i]))
    ch = ord(s[i]) - i
    ret += unichr(ch)
    i += 1
print(ret)
