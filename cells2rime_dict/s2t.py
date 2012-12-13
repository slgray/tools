#/us/bin/env python
#-*- coding: utf8 -*-

import opencc

cc = opencc.OpenCC('s2t')
print cc.convert(u'「开放中文转换」，是一个致力于中文繁简转换的项目，提供高质量词库和函数库(libopencc)。')
