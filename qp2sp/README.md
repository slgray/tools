忠哲输入法全拼词库转换双拼词库脚本
==================================

[忠哲输入法](http://bbs.zoopda.com/thread-123750-1-1.html) WebOS平台最好用的输入法没有之一

功能：将全拼的词库转换到双拼的词库，配合忠哲的脚本转换成忠哲专用脚本，可以勉强在WebOS上使用双拼。

table.py为码表，可以根据你所用的码表修改注意格式要与提供的一致

qp2sp.py使用方法:

python qp2sp.py [INPUTFILE] [OUTPUTFILE] [FILETYPE]</p>
INPUTFILE = 原来的全拼词库文件</p>
OUTPUTFILE = 输出的双拼词库</p>
FILETYPE = INPUTFILE的类型 "1"表示字库 "2"表示词库

PS:以上字库和词库的格式需与忠哲提供的词库转换包中的py目录下的格式一致

ToDo：实现真正的双拼
