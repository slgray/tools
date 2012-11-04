#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from sys import argv

script, input_file, output_file = argv
def addspace(line):
    p = re.compile('[a-z]+')
    m = p.match(line)
    end = m.end()
    s = line[0:int(end)] +' ' + line[int(end):]
    return s
f = open(input_file)
s = ''
for line in f.readlines():
    l = addspace(line)
    s += l

nf = open(output_file, 'w')
nf.write(s)
nf.close()
f.close()
