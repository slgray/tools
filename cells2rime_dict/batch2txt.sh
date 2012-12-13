#!/bin/sh
#
##################################################################
#
# 批量转化搜狗细胞词库至txt文本
#
# author: bluffstone@gmail.com / zhifeng.kuang@alipay.com
# date: 2012-10-13
#################################################################

CELLS_DIR=cells

# 删除已经存在的txt词库
rm -fr $CELLS_DIR/*.txt

# 批量把搜狗细胞词库转换为txt格式
for f in `ls ./$CELLS_DIR/*.scel`
do
	echo "文件名称：" $f
	python2 cell2txt.py $f
done

