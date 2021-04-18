#!/usr/bin/python

import sys

i = 0
s = ""
arg = sys.argv[1]
while i != len(arg):
   ch = ord(arg[i]) - i
   s =  s + chr(ch)
   i += 1
print(s)
