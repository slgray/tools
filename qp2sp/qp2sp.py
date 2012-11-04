#!/usr/bin/python
# -*- coding: utf-8 -*-
#忠哲输入法全拼转双拼脚本

from sys import argv
from table import *
import os

#input_file 全拼词库文件名
#out_file 输出双拼词库文件名
#词库的类型 1：字 2:词语
script, input_file, output_file,librarytype = argv

def addo(line):
    sline = line.split(' ')
    s0 = sline[0]
    if len(s0) ==1:
        line = 'o' + line
    return line

def addocy(line):
    sline1 = line.split(" ")
    sline2 = sline1[0].split("'")
    l0 = ''
    for l in sline2:
        if len(l) == 1:
            l = 'o' + l
        l0 = l0 + l
    return l0 + " " + sline1[1]


def tablerp(s):
    s = s.replace('er',er)
    s = s.replace('ei',ei)
    s = s.replace('ing',ing)
    s = s.replace('eng',eng)
    s = s.replace('en',en)
    s = s.replace('iong',iong)
    s = s.replace('ong',ong)
    s = s.replace('uo',uo)
    s = s.replace('ou',ou)
    s = s.replace('uai',uai)
    s = s.replace('ai',ai)
    s = s.replace('iao',iao)
    s = s.replace('ao',ao)
    s = s.replace('iang',iang)
    s = s.replace('uang',uang)
    s = s.replace('uan',uan)
    s = s.replace('ang',ang)
    s = s.replace('ian',ian)
    s = s.replace('an',an)
    s = s.replace('in',oin)
    s = s.replace('un',un)
    s = s.replace('ue',ue)
    s = s.replace('ve',ve)
    s = s.replace('ui',ui)
    s = s.replace('ia',ia)
    s = s.replace('ua',ua)
    s = s.replace('iu',iu)
    s = s.replace('ie',ie)
    s = s.replace('ch',ch)
    s = s.replace('sh',sh)
    s = s.replace('zh',zh)
    return s
#replace
f = open(input_file)
pylibrary = f.read()
pylibrary = tablerp(pylibrary)
nf = open('temp', 'w')
nf.write(pylibrary)
nf.close()

#addo
nf = open('temp')
s = ""
num = int(librarytype)

if num == 1:
    for line in nf.readlines():
        l = addo(line)
        s += l


if num == 2:
    for line in nf.readlines():
        l =addocy(line)
        s += l
finf = open(output_file, 'w')
finf.write(s)
nf.close()
finf.close()
f.close()
os.remove('temp')
