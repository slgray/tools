#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def isint(line):

    try:
        int(line[0])
        return 'Q'
    except:
        return 'A'

def changeline(line, stamp0, stamp1):
    if isint(line) == 'Q':
        line = line.split(', ')[1]
    if stamp0 == 'A':
        if stamp1 == 'Q':
            l = '\n' + line.rstrip()
        else:
            l = ',' + line.rstrip()
    else:
        l = '\t' + line.rstrip()
    return l

youdaofile = open('words.txt')
stamp1 = 'Q'
s = ""
n = 0
for line in youdaofile.readlines():
    stamp0 = stamp1
    stamp1 = isint(line)
    if n == 0:
	stamp1 = 'Q'
        l = line.split(', ')[1].rstrip()
        n = 1
    else:
        l = changeline(line, stamp0, stamp1)
    s += l
youdaofile.close()

flashcardsfile = open('flashcards.txt', 'w')
flashcardsfile.write(s)
flashcardsfile.close()
