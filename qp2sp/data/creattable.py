#!/usr/bin/python
# -*- coding: utf-8 -*-
#生成码表

from sys import argv
script, input_file = argv
def tableformate(line):
    sline = line.split('=')
    line = sline[0]+"="+"'"+sline[1].lower()
    line = line.strip()
    line += "'"+"\n"
    return line

f = open(input_file)
s = ''
for line in f.readlines():
    s += tableformate(line)
FILE = open('table.py', 'w')
FILE.write(s)
FILE.close()
f.close()
